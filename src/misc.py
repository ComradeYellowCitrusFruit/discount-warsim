import io
import math
import os
import time

### I know I could just insert this everytime I need to clear the console but for convenience this is better
def clearConsole():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')