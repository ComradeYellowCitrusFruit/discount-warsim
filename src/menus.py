### Holds menus like the main menu, pause menu, etc
from fileSystem import deleteSave, startGame
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
        startGame()
    elif input() == '2':
        print('To be added')
        clearConsole()
    elif input() == '3':
        deleteSave()