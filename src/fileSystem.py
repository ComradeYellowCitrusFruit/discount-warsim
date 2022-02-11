import os
import random
from misc import *
from menus import *

### First creates a save, different than saving
def startGame():
    savename = '.\\savefiles\\' + input('What do you want to name your save?\n')
    if os.path.exists(savename):
        if input('That name is already taken, would you like to delete that save, Y/N?   ') == 'y':
            os.remove(savename)
            savename = '.\\savefiles\\' + input('\nWhat do you want to name your save?\n')
    clearConsole()
    print('What difficulty do you want your save to be?\n')
    print('1) Little baby mode | No challenge, you start out loaded with resources and land, and everyone else is weak\n')
    print('2) Easy | Little challenge, you start out with lots of resources and land\n')
    print('3) Normal | Some challenge, you start out with the same amount of resources and land as everyone else\n')
    print('4) Hard | Large challenge, you start out with little resources and little land\n')
    print('5) Insanity | Extreme Challenge, you start out poor with only one piece of land\n')
    print('6) Pure Insanity | May God have mercy on your soul\n')
    difficulty = int(input())
    savefile = open(savename + '.ply.txt', 'x')
    with open(savename + '.ply.txt', 'x') as savefile:
        savefile.write(difficulty + '\n')
        if difficulty == 1:
            ### Player info is .ply.txt
            ### Gold
            savefile.write(random.randrange(75000,250000) + '\n')
            ### Land
            savefile.write(random.randrange(15,35) + '\n')
            ### Peasants/Soldiers/Elite Soldiers
            savefile.write(random.randrange(1000,10000) + '\n')
            savefile.write(random.randrange(500, 15000) + '\n')
            savefile.write(random.randrange(25, 500) + '\n')
            ### Rebel chance
            if random.randrange(0,1000) < 999:
                savefile.write('0\n')
            else:
                savefile.write('1\n')
            ### Foreign info lines
            ### TODO: Add naming, also add IDs
            rnd = random.randrange(10,35)
            for i in range(rnd):
                foreignfile = open(savename + '.' + i + '.ext.txt', 'x')
                with open(savename + '.ext.txt', 'x') as foreignfile:
                    foreignfile.write()
### Deletes save files
def deleteSave():
    savename = '.\\savefiles\\' + input('What is the name of the save you want to delete?   ') + '.txt'
    if os.path.exists(savename):
        os.remove(savename)
        return(1)
    else:
        print("The file does not exist")
        return(0)