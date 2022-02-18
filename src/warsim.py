### A core module so to speak of the game itself,
### Will handle all ingame functions, and also be largly intertwined with the saving and loading processes
from fileSystem import *
from misc import *
from menus import *

class country:
    def __init__(self, ID, GOLD, LAND, ESOLDIER, SOLDIER, PSOLDIER, TECH, WAR, ISPLY):
        self.id = ID
        self.gold = GOLD
        self.land = LAND
        self.elite = ESOLDIER
        self.troop = SOLDIER
        self.peasant = PSOLDIER
        self.men = self.elite + self.troop + self.peasant
        self.tech = TECH
        self.warlike = WAR
        self.isPlayer = ISPLY
    def battle(self, type, isVIC, stakes, outcome):
        if isVIC == 1:
            ### Type one is a raid, type two is a skirmish, type three is a full blown invasion
            if type == 1:
                ### Loss
                if outcome == 1:
                    self.gold -= stakes
                ### Victory
                else:
                    vict = 'yes'
                    ### Defensive victories don't have rewards
            elif type == 3:
                if outcome == 1:
                    self.land -= stakes
                ### Victory
                else:
                    vict = 'yes'
                    ### Defensive victories don't have rewards
        elif isVIC == 0:
            if type == 3:
                if outcome == 0:
                    self.land += stakes
                else:
                    deft = 'yes'
            elif type == 1:
                if outcome == 0:
                    self.gold += stakes
