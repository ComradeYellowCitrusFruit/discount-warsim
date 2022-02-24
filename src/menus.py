### Holds menus like the main menu, pause menu, etc
import time
import fileSystem
from misc import *

def mainMenu(log):
    print('1) New Game\n')
    print('2) Load save\n')
    print('3) Delete save\n')
    print('4) Quit to desktop\n')
    Input = int(input())
    if Input == 4:
        log.exit()
        quit()
    elif Input == 1:
        clearConsole()
        return(1)
    elif Input == 2:
        print('To be added')
        time.sleep(2)
        clearConsole()
    elif Input == '3':
        return(3)
def initiateMenu(log):
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
        initiateMenu()