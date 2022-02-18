### Holds menus like the main menu, pause menu, etc
from fileSystem import *
from misc import *

def mainMenu():
    print('1) New Game\n')
    print('2) Load save\n')
    print('3) Delete save\n')
    print('4) Quit to desktop\n')
    if input() == '4':
        quit()
    elif input() == '1':
        clearConsole()
        return(1)
    elif input() == '2':
        print('To be added')
        clearConsole()
    elif input() == '3':
        return(3)
def initialMenu():
    if mainMenu() == 1:
        if startGame() == 0:
            startGame()
        else:
            initialMenu()
    elif mainMenu() == 3:
        deleteSave()
    else:
        initialMenu()