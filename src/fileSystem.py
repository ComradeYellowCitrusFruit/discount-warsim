import os
import random
from misc import *

### First creates a save, different than saving
### startGame version alpha 1.0.2
def startGame():
    print('What do you want to name your save?\n')
    savename = input()
    if os.path.exists('savefiles\\' + savename + '.txt'):
        if input('That name is already taken, would you like to delete that save, Y/N?   ') == 'y':
            os.remove('savefiles\\' + savename + '.txt')
            os.remove('savefiles\\' + savename + '.ply.txt')
            os.remove('savefiles\\' + savename + 'ext.txt')
            os.remove('savefiles\\' + savename + 'war.txt')
            comb(savename)
            return 0
        else:
            print('\nWhat do you want to name your save?\n')
            savename = input()
    if os.path.exists('savefiles\\list.txt'):
        with open('savefiles\\list.txt', 'a') as savelist:
            savelist.write(savename + '\n')
    elif not os.path.exists('savefiles\\list.txt') and not os.path.exists('savefiles'):
        os.mkdir('savefiles')
        with open('savefiles\\list.txt', 'x') as savelist:
            savelist.write(savename + '\n')
    else:
        with open('savefiles\\list.txt', 'x') as savelist:
            savelist.write(savename + '\n')
    clearConsole()
    print('What difficulty do you want your save to be?\n')
    print('1) Little baby mode | No challenge, you start out loaded with resources and land, and everyone else is weak\n')
    print('2) Easy | Little challenge, you start out with lots of resources and land\n')
    print('3) Normal | Some challenge, you start out with the same amount of resources and land as everyone else\n')
    print('4) Hard | Large challenge, you start out with little resources and little land\n')
    print('5) Insanity | Extreme Challenge, you start out poor with only one piece of land\n')
    print('6) Pure Insanity | May God have mercy on your soul\n')
    difficulty = int(input())
    _savename = savename
    savename = 'savefiles\\' + _savename
    ### Index file keeps track of some save info
    with open(savename + '.txt', 'x') as indexfile:
        indexfile.write(str(difficulty) + '\n')
        with open(savename) + '.ply.txt', 'x') as savefile:
            if difficulty == 1:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(randStr(75000,250000) + '\n')
                ### Land
                savefile.write(randStr(15, 35) + '\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(randStr(1000,10000) + '\n')
                savefile.write(str(random.randrange(500, 15000)) + '\n')
                savefile.write(str(random.randrange(25, 500)) + '\n')
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
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(500, 25000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(1,15) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(50, 10000) + '\n')
                        foreignfile.write(random.randrange(50, 10000) + '\n')
                        foreignfile.write(random.randrange(0, 2500) + '\n')
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
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            elif difficulty == 2:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(random.randrange(25000,100000) + '\n')
                ### Land
                savefile.write(random.randrange(8,25) + '\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(random.randrange(500,7500) + '\n')
                savefile.write(random.randrange(250, 7500) + '\n')
                savefile.write(random.randrange(25, 400) + '\n')
                ### Tech
                ### Tech is the level your technology is at, higher is better
                if random.randrange(0,100) > 75:
                    savefile.write('10\n')
                else:
                    savefile.write('9\n')
                ### Rebel chance
                ### TODO: Add rebels
                if random.randrange(0,100) < 99:
                    savefile.write('0\n')
                else:
                    savefile.write('1\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(2000, 100000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(2,25) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(150, 10000) + '\n')
                        foreignfile.write(random.randrange(150, 10000) + '\n')
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
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            elif difficulty == 3:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(random.randrange(1000,50000) + '\n')
                ### Land
                savefile.write(random.randrange(4,20) + '\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(random.randrange(250,5000) + '\n')
                savefile.write(random.randrange(100, 5000) + '\n')
                savefile.write(random.randrange(10, 200) + '\n')
                ### Tech
                ### Tech is the level your technology is at, higher is better
                rnd = random.randrange(0,100)
                if rnd == 100:
                    savefile.write('10\n')
                elif rnd >= 90:
                    savefile.write('9\n')
                elif rnd >= 80:
                    savefile.write('8\n')
                elif rnd >= 70:
                    savefile.write('7\n')
                elif rnd >= 60:
                    savefile.write('6\n')
                elif rnd >= 50:
                    savefile.write('5\n')
                elif rnd >= 40:
                    savefile.write('4\n')
                elif rnd >= 30:
                    savefile.write('3\n')
                elif rnd >= 20:
                    savefile.write('2\n')
                else:
                    savefile.write('1\n')
                ### Rebel chance
                ### TODO: Add rebels
                if random.randrange(0,100) < 60:
                    savefile.write('0\n')
                else:
                    savefile.write('1\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(1000, 75000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(2,25) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(150, 10000) + '\n')
                        foreignfile.write(random.randrange(150, 10000) + '\n')
                        foreignfile.write(random.randrange(50, 2500) + '\n')
                        ### Tech
                        q = random.randrange(0,100)
                        if q == 100:
                            ### Renaissance
                            foreignfile.write('10\n')
                        elif q >= 90:
                            foreignfile.write('9\n')
                        elif q >= 80:
                            foreignfile.write('8\n')
                        elif q >= 70:
                            foreignfile.write('7\n')
                        elif q >= 60:
                            foreignfile.write('6\n')
                        elif q >= 50:
                            foreignfile.write('5\n')
                        elif q >= 40:
                            foreignfile.write('4\n')
                        elif q >= 30:
                            foreignfile.write('3\n')
                        elif q >= 25:
                            foreignfile.write('2\n')
                        elif q >= 20:
                            foreignfile.write('1\n')
                        else:
                            ### Tribal
                            foreignfile.write('0\n')
                        ### The most basic possible diplomacy, who they are and are not at war with
                        ### Determines how warlike they are
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            elif difficulty == 4:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(random.randrange(250,2500) + '\n')
                ### Land
                savefile.write(random.randrange(2,8) + '\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(random.randrange(100,2500) + '\n')
                savefile.write(random.randrange(50, 2500) + '\n')
                savefile.write(random.randrange(0, 100) + '\n')
                ### Tech
                ### Tech is the level your technology is at, higher is better
                rnd = random.randrange(0,100)
                if rnd >= 95:
                    savefile.write('9\n')
                elif rnd >= 75:
                    savefile.write('8\n')
                elif rnd >= 70:
                    savefile.write('7\n')
                elif rnd >= 60:
                    savefile.write('6\n')
                elif rnd >= 40:
                    savefile.write('5\n')
                elif rnd >= 20:
                    savefile.write('4\n')
                elif rnd >= 15:
                    savefile.write('3\n')
                elif rnd >= 10:
                    savefile.write('2\n')
                else:
                    savefile.write('1\n')
                ### Rebel chance
                ### TODO: Add rebels
                if random.randrange(0,100) < 20:
                    savefile.write('0\n')
                else:
                    savefile.write('1\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(1000, 175000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(5,25) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(200, 25000) + '\n')
                        foreignfile.write(random.randrange(200, 25000) + '\n')
                        foreignfile.write(random.randrange(100, 5000) + '\n')
                        ### Tech
                        q = random.randrange(0,100)
                        if q >= 95:
                            ### Renaissance
                            foreignfile.write('10\n')
                        elif q >= 90:
                            foreignfile.write('9\n')
                        elif q >= 80:
                            foreignfile.write('8\n')
                        elif q >= 70:
                            foreignfile.write('7\n')
                        elif q >= 50:
                            foreignfile.write('6\n')
                        elif q >= 30:
                            foreignfile.write('5\n')
                        elif q >= 20:
                            foreignfile.write('4\n')
                        elif q >= 15:
                            foreignfile.write('3\n')
                        elif q >= 10:
                            foreignfile.write('2\n')
                        elif q >= 5:
                            foreignfile.write('1\n')
                        else:
                            ### Tribal
                            foreignfile.write('0\n')
                        ### The most basic possible diplomacy, who they are and are not at war with
                        ### Determines how warlike they are
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            elif difficulty == 5:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(random.randrange(50,750) + '\n')
                ### Land
                savefile.write('1\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(random.randrange(100,2500) + '\n')
                savefile.write(random.randrange(50, 2500) + '\n')
                savefile.write(random.randrange(0, 50) + '\n')
                ### Tech
                ### Tech is the level your technology is at, higher is better
                rnd = random.randrange(0,100)
                if rnd >= 95:
                    savefile.write('8\n')
                elif rnd >= 90:
                    savefile.write('7\n')
                elif rnd >= 80:
                    savefile.write('6\n')
                elif rnd >= 75:
                    savefile.write('5\n')
                elif rnd >= 50:
                    savefile.write('4\n')
                elif rnd >= 35:
                    savefile.write('3\n')
                elif rnd >= 30:
                    savefile.write('2\n')
                elif rnd >= 20:
                    savefile.write('1\n')
                else:
                    savefile.write('0\n')
                ### Because I am a merciful person, this difficulty will not have rebels, you can thank me later
                ### TODO: Add rebels
                savefile.write('0\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(2500, 200000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(5,25) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(500, 25000) + '\n')
                        foreignfile.write(random.randrange(500, 25000) + '\n')
                        foreignfile.write(random.randrange(500, 5000) + '\n')
                        ### Tech
                        q = random.randrange(0,100)
                        if q >= 85:
                            ### Renaissance
                            foreignfile.write('10\n')
                        elif q >= 80:
                            foreignfile.write('9\n')
                        elif q >= 75:
                            foreignfile.write('8\n')
                        elif q >= 65:
                            foreignfile.write('7\n')
                        elif q >= 55:
                            foreignfile.write('6\n')
                        elif q >= 35:
                            foreignfile.write('5\n')
                        elif q >= 15:
                            foreignfile.write('4\n')
                        elif q >= 10:
                            foreignfile.write('3\n')
                        else:
                            foreignfile.write('2\n')
                        ### The most basic possible diplomacy, who they are and are not at war with
                        ### Determines how warlike they are
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            elif difficulty == 6:
                ### Player info is .ply.txt
                ### Gold
                savefile.write(random.randrange(1,500) + '\n')
                ### Land
                savefile.write('1\n')
                ### Peasants/Soldiers/Elite Soldiers
                savefile.write(random.randrange(10,250) + '\n')
                savefile.write(random.randrange(0, 100) + '\n')
                savefile.write(random.randrange(0, 10) + '\n')
                ### Tech
                ### Tech is the level your technology is at, higher is better
                rnd = random.randrange(0,100)
                if rnd >= 95:
                    savefile.write('7\n')
                elif rnd >= 90:
                    savefile.write('6\n')
                elif rnd >= 80:
                    savefile.write('5\n')
                elif rnd >= 70:
                    savefile.write('4\n')
                elif rnd >= 60:
                    savefile.write('3\n')
                elif rnd >= 40:
                    savefile.write('2\n')
                elif rnd >= 20:
                    savefile.write('1\n')
                else:
                    savefile.write('0\n')
                ### You can have a little mercy, as a treat
                ### TODO: Add rebels
                if random.randrange(0,100) < 50:
                    savefile.write('0\n')
                else:
                    savefile.write('1\n')
                ### TODO: Add naming
                ### TODO: Add Diplomacy
                rnd = random.randrange(10,35)
                indexfile.write(rnd + '\n')
                for i in range(rnd):
                    with open(savename + '.ext.txt', 'x') as foreignfile:
                        ### Gold
                        foreignfile.write(random.randrange(2500, 500000) + '\n')
                        ### Land
                        foreignfile.write(random.randrange(5,50) + '\n')
                        ### Peasants/Soldiers/Elite Soldiers
                        foreignfile.write(random.randrange(500, 50000) + '\n')
                        foreignfile.write(random.randrange(500, 50000) + '\n')
                        foreignfile.write(random.randrange(500, 10000) + '\n')
                        ### Tech
                        q = random.randrange(0,100)
                        if q >= 85:
                            ### Renaissance
                            foreignfile.write('10\n')
                        elif q >= 70:
                            foreignfile.write('9\n')
                        elif q >= 65:
                            foreignfile.write('8\n')
                        elif q >= 50:
                            foreignfile.write('7\n')
                        elif q >= 25:
                            foreignfile.write('6\n')
                        elif q >= 15:
                            foreignfile.write('5\n')
                        elif q >= 5:
                            foreignfile.write('4\n')
                        else:
                            foreignfile.write('3\n')
                        ### The most basic possible diplomacy, who they are and are not at war with
                        ### Determines how warlike they are
                        w = warlikeGen(foreignfile, rnd, savename, i)
                        foreignfile.write('<---END OF FILE--->')
                ### END OF FOREIGN FILE
            savefile.write('<---END OF FILE--->')
        indexfile.write('<---END OF FILE--->')
    return 1
### Deletes save files
### TODO: Update deleteSave()
def warlikeGen(foreignfile, rnd, savename, i):
    q = random.randrange(1, 200)
    if q >= 175:
        ### Fights everyone
        return 8
    elif q >= 150 and q <= 174:
        ### Highly prone to wars
        return 7
    elif q >= 125 and q <= 149:
        ### Still prone to wars
        return 6
    elif q >= 100 and q <= 124:
        ### Easy to agitate
        return 5
    elif q >= 75 and q <= 99:
        ### Will go to war if necessary
        w = 4
    elif q >= 50 and q <= 74:
        ### Reluctant to go to war
        w = 3
    elif q >= 25 and q <= 49:
        ### Will only go to war if absolutely necessary
        w = 2
    else:
        ### Will not attack ever
        w = 1
    foreignfile.write(w + '\n')
    if w == 8:
        with open(savename + '.' + i + '.war.txt', 'x') as warfile:
            for r in rnd:
                if not r == i:
                    warfile.write('1\n')
                else:
                    warfile.write('self\n')
            warfile.write('<---END OF FILE--->')
    elif w == 7:
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
        with open(savename + '.' + i + '.war.txt', 'x') as warfile:
            for r in rnd + 1:
                if not r == i:
                    warfile.write('0\n')
                else:
                    warfile.write('self\n')
            warfile.write('<---END OF FILE--->')
def deleteSave():
    print('What is the name of the save you want to delete?   ')
    savename = input()
    if os.path.exists('savefiles\\' + savename + '.txt'):
        os.remove('savefiles\\' + savename + '.txt')
        os.remove('savefiles\\' + savename + '.ply.txt')
        os.remove('savefiles\\' + savename + 'ext.txt')
        os.remove('savefiles\\' + savename + 'war.txt')
        comb(savename)
        return(1)
    else:
        print("\nThe file does not exist")
        return(0)
def loadSave():
    print('Which save would you like to load?\n')
def comb(savename):
    savelist = open('savefiles\\list.txt', 'r')
    namelist = savelist.readlines()
    savelist.close()
    with open('savefiles\\list.txt', 'w') as savelist_:
        for name in namelist:
            if not name.strip('\n') == savename:
                savelist_.write(name)