import os
import random
from misc import *
from menus import *

### First creates a save, different than saving
def startGame():
    savename = '.\\savefiles\\' + input('What do you want to name your save?\n')
    if os.path.exists(savename + '.txt'):
        if input('That name is already taken, would you like to delete that save, Y/N?   ') == 'y':
            os.remove(savename + '.txt')
            os.remove(savename + '.ply.txt')
            os.remove(savename + 'ext.txt')
            os.remove(savename + 'war.txt')
        else:
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
    ### Index file keeps track of some save info
    indexfile = open(savename + '.txt', 'x')
    with open(savename + '.txt', 'x') as indexfile:
        indexfile.write(difficulty + '\n')
        savefile = open(savename + '.ply.txt', 'x')
        with open(savename + '.ply.txt', 'x') as savefile:
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
                ### Tech
                ### Tech is the level your technology is at, higher is better
                if random.randrange(0,100000) > 99999:
                    savefile.write('10\n')
                else:
                    savefile.write('9\n')
                ### Rebel chance
                ### TODO: Add rebels
                if random.randrange(0,1000) < 999:
                    savefile.write('0\n')
                else:
                    savefile.write('1\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    foreignfile = open(savename + '.' + i + '.ext.txt', 'x')
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(2000, 75000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(5,15) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(100, 10000) + '\n')
                        foreignfile.write(random.randrange(100, 10000) + '\n')
                        foreignfile.write(random.randrange(50, 2500) + '\n')
                        ### Tech
                        q = random.randrange(0,200)
                        if q >= 199:
                            ### Renaissance
                            foreignfile.write('10\n')
                        elif q >= 176 and q < 199:
                            foreignfile.write('9\n')
                        elif q >= 151 and q <= 175:
                            foreignfile.write('8\n')
                        elif q >= 126 and q <= 150:
                            foreignfile.write('7\n')
                        elif q >= 101 and q <= 125:
                            foreignfile.write('6\n')
                        elif q >= 76 and q <= 100:
                            foreignfile.write('5\n')
                        elif q >= 46 and q <= 75:
                            foreignfile.write('4\n')
                        elif q >= 41 and q <= 45:
                            foreignfile.write('3\n')
                        elif q >= 36 and q <= 40:
                            foreignfile.write('2\n')
                        elif q >= 31 and q <= 35:
                            foreignfile.write('1\n')
                        elif q >= 0 and q <= 30:
                            ### Tribal
                            foreignfile.write('0\n')
                        ### The most basic possible diplomacy, who they are and are not at war with
                        ### Determines how warlike they are
                        q = random.randrange(1, 200)
                        if q >= 175:
                            ### Fights everyone
                            foreignfile.write('8\n')
                            w = 8
                        elif q >= 150 and q <= 174:
                            ### Highly prone to wars
                            foreignfile.write('7\n')
                            w = 7
                        elif q >= 125 and q <= 149:
                            ### Still prone to wars
                            foreignfile.write('6\n')
                            w = 6
                        elif q >= 100 and q <= 124:
                            ### Easy to agitate
                            foreignfile.write('5\n')
                        elif q >= 75 and q <= 99:
                            ### Will go to war if necessary
                            foreignfile.write('4\n')
                            w = 4
                        elif q >= 50 and q <= 74:
                            ### Reluctant to go to war
                            foreignfile.write('3\n')
                            w = 3
                        elif q >= 25 and q <= 49:
                            ### Will only go to war if absolutely necessary
                            foreignfile.write('2\n')
                            w = 2
                        elif q >= 0 and q <= 24:
                            ### Will not attack ever
                            foreignfile.write('1\n')
                            w = 1
                        if w == 8:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd:
                                    if not r == i:
                                        warfile.write('1\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 7:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 5:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 6:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 20:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 5:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 35:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 4:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 50:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 3:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 75:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 2:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        if random.randrange(1,100) > 90:
                                            warfile.write('1\n')
                                        else:
                                            warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        elif w == 1:
                            warfile = open(savename + '.' + i + '.war.txt', 'x')
                            with open(savename + '.' + i + '.war.txt', 'x') as warfile:
                                for r in rnd + 1:
                                    if not r == i:
                                        warfile.write('0\n')
                                    else:
                                        warfile.write('self\n')
                                warfile.write('<---END OF FILE--->')
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            savefile.write('<---END OF FILE--->')
        indexfile.write('<---END OF FILE--->')
### Deletes save files
def deleteSave():
    savename = '.\\savefiles\\' + input('What is the name of the save you want to delete?   ') + '.txt'
    if os.path.exists(savename):
        os.remove(savename)
        return(1)
    else:
        print("The file does not exist")
        return(0)