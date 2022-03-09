### Holds menus like the main menu, pause menu, etc
import sys
import time
import fileSystem
import re
import playsound
from misc import *
import lemon16_85.Lemon16_85 as Base16_85

def mainMenu(log : fileSystem.logger):
    print('1) New Game\n')
    print('2) Load save\n')
    print('3) Delete save\n')
    print('4) Quit to desktop\n')
    Input = input()
    if re.search(Regex.UKRAINE, Input.lower()):
        EasterEggs.Ukraine()
        ### TODO: fix ukraine anthem not playing
        """
        if not os.path.exists('resources//ukraine_anthem.mp3'):
            TmP = open('resources//ukraine_anthem.mp3', 'xb')
            TmP.write(Base16_85.Decode(tmp, False))
            TmP.close()
        try:
            playsound.playsound('resources//ukraine_anthem.mp3')
        except:
           print('Can\'t open ukraine_anthem.mp3') 
        """
        print('Press any key to continue...    ')
        input()
        initiateMenu(log)
    if Input == 4:
        log.exit()
        sys.exit()
    elif Input == 1:
        clearConsole()
        return(1)
    elif Input == 2:
        print('To be added')
        time.sleep(2)
        clearConsole()
    elif Input == '3':
        return(3)
def initiateMenu(log : fileSystem.logger):
    initiate = mainMenu(log)
    if initiate == 1:
        fileSystem.startGame(log)
        clearConsole()
        for i in range(200):
            print("IT WORKED!\n")
        time.sleep(5)
        clearConsole()
        initiateMenu()
    elif initiate == 3:
        fileSystem.deleteSave()
    else:
        initiateMenu(log)