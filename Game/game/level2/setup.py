import cx_Freeze
from cx_Freeze import *

setup(
    name = "Smashing bob_Game",
    options = {"build.exe": {"packages": ['pygame', 'random'], "zip_include_packages": ["*"], "zip_exclude_packages": ['scipy', 'numpy']},},
    executables = [
        Executable("_l2.py",),
        Executable("Player.py",),
        Executable("Bullet.py",),
        Executable("Enemy.py",),

        
        ]
    
    
    
    )