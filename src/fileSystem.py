import io
import math
import os
import time
from misc import *
from menus import *

### First creates a save, different than saving
def startGame():
    savename = '.\\savefiles\\' + input('What do you want to name your save?\n') + '.txt'
    if os.path.exists(savename):
        if input('That name is already taken, would you like to delete that save, Y/N?   ') == 'y':
            os.remove(savename)
            savename = '.\\savefiles\\' + input('\nWhat do you want to name your save?\n') + '.txt'
    clearConsole()
    print('What difficulty do you want your save to be?\n')
    print('1) Little baby mode | No challenge, you start out loaded with resources and land, and everyone else is weak\n')
    print('2) Easy | Little challenge, you start out with lots of resources and land\n')
    print('3) Normal | Some challenge, you start out with the same amount of resources and land as everyone else\n')
    difficulty = input()
### Deletes save files
def deleteSave():
    savename = '.\\savefiles\\' + input('What is the name of the save you want to delete?   ') + '.txt'
    if os.path.exists(savename):
        os.remove(savename)
        return(1)
    else:
        print("The file does not exist")
        return(0)