import numpy as np
import random
import pygame
import sys
import math

blue = (0,0,255)
black= (0,0,0)
red = (255,0,0)
yellow= (255,255,0)

row_count = 6
column_count = 7

PLAYER = 0
AI = 1

null = 0
p_piece = 1
ai_piece = 2

WINDOW_LENGTH = 4

#creates a null matrix of size 6x7
def game_window():
	game = np.zeros((row_count,column_count))
	return game

#function assigns the piece(1 or 2) number to the position chosen 
def drop_piece(game, row, col, piece):
	game[row][col] = piece

#if the topmost row of that paricular column is 0, it indicates that the position is valid
def check_location(game, col):
	return game[row_count-1][col] == 0

#checks if that particular row is valid for the chosen position 
def get_next_open_row(game, col):
	for r in range(row_count):
		if game[r][col] == 0:
			return r

#flips the entire matrix 
def print_game(game):
	print(np.flip(game, 0))

#checks for four continous pieces(horizontally or vertically or diagnolly) 
def winning_move(game, piece):

	# horizontal 
	for c in range(column_count-3):
		for r in range(row_count):
			if game[r][c] == piece and game[r][c+1] == piece and game[r][c+2] == piece and game[r][c+3] == piece:
				return True

	#vertical
	for c in range(column_count):
		for r in range(row_count-3):
			if game[r][c] == piece and game[r+1][c] == piece and game[r+2][c] == piece and game[r+3][c] == piece:
				return True

	#positively sloped diaganols
	for c in range(column_count-3):
		for r in range(row_count-3):
			if game[r][c] == piece and game[r+1][c+1] == piece and game[r+2][c+2] == piece and game[r+3][c+3] == piece:
				return True

	#negatively sloped diaganols
	for c in range(column_count-3):
		for r in range(3, row_count):
			if game[r][c] == piece and game[r-1][c+1] == piece and game[r-2][c+2] == piece and game[r-3][c+3] == piece:
				return True

def evaluate_window(window, piece):
	score = 0
	opp_piece = p_piece
	if piece == p_piece:
		opp_piece = ai_piece

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(null) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(null) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(null) == 1:
		score -= 4

	return score

def score_position(game, piece):
	score = 0

	# Score center column
	center_array = [int(i) for i in list(game[:, column_count//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	#Score Horizontal
	for r in range(row_count):
		row_array = [int(i) for i in list(game[r,:])]
		for c in range(column_count-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	# Score Vertical
	for c in range(column_count):
		col_array = [int(i) for i in list(game[:,c])]
		for r in range(row_count-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	# Score posiive sloped diagonal
	for r in range(row_count-3):
		for c in range(column_count-3):
			window = [game[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(row_count-3):
		for c in range(column_count-3):
			window = [game[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score

def is_terminal_node(game):
	return winning_move(game, p_piece) or winning_move(game, ai_piece) or len(get_valid_locations(game)) == 0

def minimax(game, depth, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(game)
	is_terminal = is_terminal_node(game)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(game, ai_piece):
				return (None, 100000000000000)
			elif winning_move(game, p_piece):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(game, ai_piece))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(game, col)
			b_copy = game.copy()
			drop_piece(b_copy, row, col, ai_piece)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(game, col)
			b_copy = game.copy()
			drop_piece(b_copy, row, col, p_piece)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(game):
	valid_locations = []
	for col in range(column_count):
		if check_location(game, col):
			valid_locations.append(col)
	return valid_locations

def pick_best_move(game, piece):

	valid_locations = get_valid_locations(game)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(game, col)
		temp_game = game.copy()
		drop_piece(temp_game, row, col, piece)
		score = score_position(temp_game, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col

def draw_game(game):
	for c in range(column_count):
		for r in range(row_count):
			pygame.draw.rect(screen, blue, (c*square_size, r*square_size+square_size, square_size, square_size))
			pygame.draw.circle(screen, black, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), RADIUS)
	
	for c in range(column_count):
		for r in range(row_count):		
			if game[r][c] == p_piece:
				pygame.draw.circle(screen, red, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), RADIUS)
			elif game[r][c] == ai_piece: 
				pygame.draw.circle(screen, yellow, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), RADIUS)
	pygame.display.update()

game = game_window()
print_game(game)
game_over = False

pygame.init()

square_size = 100

width = column_count * square_size
height = (row_count+1) * square_size

size = (width, height)

RADIUS = int(square_size/2 - 5)

screen = pygame.display.set_mode(size)
draw_game(game)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

turn = random.randint(PLAYER, AI)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, black, (0,0, width, square_size))
			posx = event.pos[0]
			if turn == PLAYER:
				pygame.draw.circle(screen, red, (posx, int(square_size/2)), RADIUS)

		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, black, (0,0, width, square_size))
			# Ask for Player 1 Input
			if turn == PLAYER:
				posx = event.pos[0]
				col = int(math.floor(posx/square_size))

				if check_location(game, col):
					row = get_next_open_row(game, col)
					drop_piece(game, row, col, p_piece)

					if winning_move(game, p_piece):
						label = myfont.render("Player 1 wins!!", 1, red)
						screen.blit(label, (40,10))
						game_over = True

					turn += 1
					turn = turn % 2

					print_game(game)
					draw_game(game)


	#Ask for Player 2 Input
	if turn == AI and not game_over:				

		col, minimax_score = minimax(game, 5, -math.inf, math.inf, True)

		if check_location(game, col):
			#pygame.time.wait(500)
			row = get_next_open_row(game, col)
			drop_piece(game, row, col, ai_piece)

			if winning_move(game, ai_piece):
				label = myfont.render("Computer wins!!", 1, yellow)
				screen.blit(label, (40,10))
				game_over = True

			print_game(game)
			draw_game(game)

			turn += 1
			turn = turn % 2

	if game_over:
		pygame.time.wait(3000)
