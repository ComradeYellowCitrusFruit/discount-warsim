import os
import random

def clearConsole():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def randStr(min, max):
    return str(random.randrange(min, max))