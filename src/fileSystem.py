import os
import random
import time
import warsim
import lemon16_85.warsim16_85 as subFS
import lemon16_85.Lemon16_85
from misc import *

### First creates a save, different than saving
### startGame version alpha 1.0.2
def startGame(log):
    save = subFS.save()
    print('What do you want to name your save?\n')
    savename = input()
    if os.path.exists('savefiles\\' + savename + '.warsim'):
        if input('That name is already taken, would you like to delete that save, Y/N?   ') == 'y' or input('That name is already taken, would you like to delete that save, Y/N?   ') == 'Y':
            log.uniqueLog('Error: Filename ' + savename + ' is already taken')
            os.remove('savefiles\\' + savename + '.warsim')
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
    print('What would you like to name your country:\n')
    name = input()
    ### Index file keeps track of some save info
    with open(savename + '.warsim', 'xb') as savefile:
        ind = [8, difficulty]
        ply = [name]
        if difficulty == 1:
            ply.append(randStr(75000,250000))
            ply.append(randStr(15, 35))
            ply.append(randStr(25, 500))
            ply.append(randStr(500, 15000))
            ply.append(randStr(1000,10000))
            if random.randrange(0,100000) < 99999:
                ply.append('10')
            else:
                ply.append('9')
            if random.randrange(0,1000) < 999:
                ind.append('0')
            else:
                ind.append('1')
            save.playerCompile(ply)
            save.indexCompile(ind)
            for i in range(ind[0]):
                fgn = [i, 'Placeholder #' + str(i)]
                fgn.append(randStr(500, 25000))
                fgn.append(randStr(1,15))
                fgn.append(randStr(0, 2500))
                fgn.append(randStr(50, 10000))
                fgn.append(randStr(50, 10000))
                q = random.randrange(0,200)
                if q >= 199:
                    ### Renaissance
                    fgn.append(10)
                elif q >= 176 and q < 199:
                    fgn.append(9)
                elif q >= 151 and q <= 175:
                    fgn.append(8)
                elif q >= 126 and q <= 150:
                    fgn.append(7)
                elif q >= 101 and q <= 125:
                    fgn.append(6)
                elif q >= 76 and q <= 100:
                    fgn.append(5)
                elif q >= 46 and q <= 75:
                    fgn.append(4)
                elif q >= 41 and q <= 45:
                    fgn.append(3)
                elif q >= 36 and q <= 40:
                    fgn.append(2)
                elif q >= 31 and q <= 35:
                    fgn.append(1)
                elif q >= 0 and q <= 30:
                    ### Tribal
                    fgn.append(0)
                save.foreignCompile(fgn)
            save.finalCompile()
        elif difficulty == 2:
            ply.append(randStr(25000,100000))
            ply.append(randStr(10, 25))
            ply.append(randStr(25, 500))
            ply.append(randStr(500, 10000))
            ply.append(randStr(1000,10000))
            if random.randrange(0,100) < 99:
                ply.append('10')
            else:
                ply.append('9')
            if random.randrange(0,100) < 99:
                ind.append('0')
            else:
                ind.append('1')
            save.playerCompile(ply)
            save.indexCompile(ind)
            for i in range(ind[0]):
                fgn = [i, 'Placeholder #' + str(i)]
                fgn.append(randStr(1000, 50000))
                fgn.append(randStr(1,15))
                fgn.append(randStr(0, 2500))
                fgn.append(randStr(50, 10000))
                fgn.append(randStr(50, 10000))
                q = random.randrange(0,200)
                if q >= 199:
                    ### Renaissance
                    fgn.append(10)
                elif q >= 176 and q < 199:
                    fgn.append(9)
                elif q >= 151 and q <= 175:
                    fgn.append(8)
                elif q >= 126 and q <= 150:
                    fgn.append(7)
                elif q >= 101 and q <= 125:
                    fgn.append(6)
                elif q >= 76 and q <= 100:
                    fgn.append(5)
                elif q >= 46 and q <= 75:
                    fgn.append(4)
                elif q >= 41 and q <= 45:
                    fgn.append(3)
                elif q >= 36 and q <= 40:
                    fgn.append(2)
                elif q >= 31 and q <= 35:
                    fgn.append(1)
                elif q >= 0 and q <= 30:
                    ### Tribal
                    fgn.append(0)
                save.foreignCompile(fgn)
            save.finalCompile()
        elif difficulty == 3:
            ply.append(randStr(5000,25000))
            ply.append(randStr(5, 15))
            ply.append(randStr(10, 250))
            ply.append(randStr(250, 5000))
            ply.append(randStr(500,7500))
            rnd = random.randrange(0,100)
            if rnd == 100:
                ply.append('10')
            elif rnd >= 90:
                ply.append('9')
            elif rnd >= 80:
                ply.append('8')
            elif rnd >= 70:
                ply.append('7')
            elif rnd >= 60:
                ply.append('6')
            elif rnd >= 50:
                ply.append('5')
            elif rnd >= 40:
                ply.append('4')
            elif rnd >= 30:
                ply.append('3')
            elif rnd >= 20:
                ply.append('2')
            else:
                ply.append('1')
            if random.randrange(0,100) <= 50:
                ind.append('0')
            else:
                ind.append('1')
            save.playerCompile(ply)
            save.indexCompile(ind)
            for i in range(ind[0]):
                fgn = [i, 'Placeholder #' + str(i)]
                fgn.append(randStr(1000, 50000))
                fgn.append(randStr(1,15))
                fgn.append(randStr(0, 2500))
                fgn.append(randStr(250, 15000))
                fgn.append(randStr(500, 20000))
                q = random.randrange(0,200)
                if q >= 199:
                    ### Renaissance
                    fgn.append(10)
                elif q >= 176 and q < 199:
                    fgn.append(9)
                elif q >= 151 and q <= 175:
                    fgn.append(8)
                elif q >= 126 and q <= 150:
                    fgn.append(7)
                elif q >= 101 and q <= 125:
                    fgn.append(6)
                elif q >= 76 and q <= 100:
                    fgn.append(5)
                elif q >= 46 and q <= 75:
                    fgn.append(4)
                elif q >= 41 and q <= 45:
                    fgn.append(3)
                elif q >= 36 and q <= 40:
                    fgn.append(2)
                elif q >= 31 and q <= 35:
                    fgn.append(1)
                elif q >= 0 and q <= 30:
                    ### Tribal
                    fgn.append(0)
                save.foreignCompile(fgn)
            save.finalCompile()
        elif difficulty == 4:
            ply.append(randStr(1000,10000))
            ply.append(randStr(2, 10))
            ply.append(randStr(5, 125))
            ply.append(randStr(100, 2500))
            ply.append(randStr(250,5000))
            rnd = random.randrange(0,100)
            if rnd >= 95:
                ply.append('9')
            elif rnd >= 75:
                ply.append('8')
            elif rnd >= 70:
                ply.append('7')
            elif rnd >= 60:
                ply.append('6')
            elif rnd >= 40:
                ply.append('5')
            elif rnd >= 20:
                ply.append('4')
            elif rnd >= 15:
                ply.append('3')
            elif rnd >= 10:
                ply.append('2')
            else:
                ply.append('1')
            if random.randrange(0,100) <= 50:
                ind.append('0')
            else:
                ind.append('1')
            save.playerCompile(ply)
            save.indexCompile(ind)
            for i in range(ind[0]):
                fgn = [i, 'Placeholder #' + str(i)]
                fgn.append(randStr(2000, 75000))
                fgn.append(randStr(5,15))
                fgn.append(randStr(250, 2500))
                fgn.append(randStr(500, 25000))
                fgn.append(randStr(500, 35000))
                q = random.randrange(0,200)
                if q >= 199:
                    ### Renaissance
                    fgn.append(10)
                elif q >= 176 and q < 199:
                    fgn.append(9)
                elif q >= 151 and q <= 175:
                    fgn.append(8)
                elif q >= 126 and q <= 150:
                    fgn.append(7)
                elif q >= 101 and q <= 125:
                    fgn.append(6)
                elif q >= 76 and q <= 100:
                    fgn.append(5)
                elif q >= 46 and q <= 75:
                    fgn.append(4)
                elif q >= 41 and q <= 45:
                    fgn.append(3)
                elif q >= 36 and q <= 40:
                    fgn.append(2)
                elif q >= 31 and q <= 35:
                    fgn.append(1)
                elif q >= 0 and q <= 30:
                    ### Tribal
                    fgn.append(0)
                save.foreignCompile(fgn)
            save.finalCompile()
        savefile.write(save.final)
        savefile.close
### Deletes save files
def deleteSave(log):
    print('What is the name of the save you want to delete?   ')
    savename = input()
    log.uniqueLog('Deleting save file ' + savename)
    if os.path.exists('savefiles\\' + savename + '.warsim'):
        os.remove('savefiles\\' + savename + '.warsim')
        comb(savename)
        log.uniqueLog('Save file ' + savename + ' deleted')
        return(1)
    else:
        print("\nThe file does not exist")
        log.uniqueLog('Save file ' + savename + ' did not exist')
        return(0)
def loadSave(log):
    print('Which save would you like to load?\n')
def comb(savename, log):
    savelist = open('savefiles\\list.txt', 'r')
    namelist = savelist.readlines()
    savelist.close()
    with open('savefiles\\list.txt', 'w') as savelist_:
        for name in namelist:
            if not name.strip('\n') == savename:
                log.uniqueLog('Combed ' + savename + ' out of the save list')
                savelist_.write(name)
class logger:
    def __init__(self):
        if os.path.exists('savefiles\\log.txt'):
            logfile = open('savefiles\\log.txt', 'a')
            logfile.write(time.asctime() + ': New Session initated\n')
            logfile.close()
            self.current = [time.asctime() + ': New Session initated']
            logreader = open('savefiles\\log.txt', 'r')
            self.all = logreader.readlines()
        else:
            logfile = open('savefiles\\log.txt', 'x')
            logfile.write(time.asctime() + ': First session initiated\n')
            logfile.close()
            self.current = [time.asctime() + ': First Session initated']
            self.initTime = time.asctime() + ': First Session initated'
            self.sessionCount = 0
        self.path = 'savefiles\\log.txt'
    ### Called in the event of a graceful exit sequence
    def exit(self):
        logfile = open(self.path, 'a')
        logfile.write(time.asctime() + ': Session shutdown\n')
        logfile.close()
    def uniqueLog(self, msg):
        logfile = open(self.path, 'a')
        logfile.write(time.asctime() + ': ' + msg + '\n')
        logfile.close()
    def uniqueLogs(self, msgs):
        logfile = open(self.path, 'a')
        for msg in msgs:
            logfile.write(time.asctime() + ': ' + msg + '\n')
        logfile.close()
    def getCurrent(self):
        for log in self.current:
            print(log + '\n')
        return self.current
    def getAll(self):
        self.All(False)
        self.all = list(self.all)
        for log in self.all:
            print(log + '\n')
        self.All(True)
    def All(self, mute):
        if mute == False:
            logfile = open(self.path, 'a')
            logfile.write(time.asctime() + ': Fetched logs')
        logfile.close()
        logread = open(self.path, 'r')
        self.all = logread.readlines()
        for i in range(len(self.all)):
            if i == 0:
                logStr = self.all[i]
            else:
                logStr += self.all[i]
        self.all = logStr
    def Current(self):
        self.All(False)
        logfile = open(self.path, 'a')
        logfile.write(time.asctime() + ': Fetched current session')
        self.All(True)
        logfile.close()
        log = self.all.split(self.initTime + ': New Session initated\n')
        self.current = list(self.initTime + ': New Session initated\n' + log[1])
