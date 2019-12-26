from subprocess import call

print("\t\t\t\t\t\t\tWelcome from the Smashing Bob community!\n")
print("\t\t\t\t\t\t\tIf you want to play The Easy level enter 1\n")
print("\t\t\t\t\t\t\tIf you want to play The Medium level enter 2\n")
print("\t\t\t\t\t\t\tIf you want to play The Hard level enter 3\n")
a=input("Enter your option")
while (True):
    if (a==1 or a==2 or a==3):
        if (a==1):
            call(["python3","level1/game.py"])
        if (a==2):
            call(["python3","level2/_l2.py"])
        if (a==3):
            call(["python3","level3/_l3.py"])
	break
            
    
