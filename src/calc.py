### Does some more complex calculations
### Most of said calculations will relate to things like warscore and battles and shit
import random
import math
from warsim import *

class warscoreCalc:
    def __init__(self, elite, troop, peasant, skill, tech):
        self.elite = elite
        self.troop = troop
        self.peasant = peasant
        ### TODO: Add generals, and skill
        self.skill = skill
        self.tech = tech
    def totalWarscore(self):
        eliteScore = self.elite * 300
        troopScore = self.troop * 150
        peasantMulti = random.randrange(50/3,25) + random.randrange(50/3,25) + random.randrange(50/3,25)
        peasantScore = self.peasant * peasantMulti
        totalScore = eliteScore + troopScore + peasantScore
        ### Since skill is representated as a one to two digit number it will be divided by 10 to get a decimal answer
        if self.tech == 0:
            totalScore *= .5 * (self.skill/10)
        else:
            totalScore *= (self.skill/10)
        if self.tech == 8:
            return totalScore * 2
        elif self.tech == 7:
            return totalScore * 1.75
        elif self.tech == 6:
            return totalScore * 1.5
        elif self.tech == 5:
            return totalScore * 1.25
        elif self.tech == 4:
            return totalScore
        elif self.tech == 3:
            return totalScore * .75
        elif self.tech == 2:
            return totalScore * .5
        elif self.tech == 1:
            return totalScore * .25
        elif self.tech == 0:
            return totalScore * .1
    def eliteWarscore(self):
        eliteScore = self.elite * 300
        if self.tech == 0:
            eliteScore *= .5 * (self.skill/10)
        else:
            eliteScore *= (self.skill/10)
        if self.tech == 8:
            return eliteScore * 2
        elif self.tech == 7:
            return eliteScore * 1.75
        elif self.tech == 6:
            return eliteScore * 1.5
        elif self.tech == 5:
            return eliteScore * 1.25
        elif self.tech == 4:
            return eliteScore
        elif self.tech == 3:
            return eliteScore * .75
        elif self.tech == 2:
            return eliteScore * .5
        elif self.tech == 1:
            return eliteScore * .25
        elif self.tech == 0:
            return eliteScore * .1
    def troopWarscore(self):
        troopScore = self.troop * 300
        if self.tech == 0:
            troopScore *= .5 * (self.skill/10)
        else:
            troopScore *= (self.skill/10)
        if self.tech == 8:
            return troopScore * 2
        elif self.tech == 7:
            return troopScore * 1.75
        elif self.tech == 6:
            return troopScore * 1.5
        elif self.tech == 5:
            return troopScore * 1.25
        elif self.tech == 4:
            return troopScore
        elif self.tech == 3:
            return troopScore * .75
        elif self.tech == 2:
            return troopScore * .5
        elif self.tech == 1:
            return troopScore * .25
        elif self.tech == 0:
            return troopScore * .1
    def peasantWarscore(self):
        peasantScore = self.troop * 300
        if self.tech == 0:
            peasantScore *= .5 * (self.skill/10)
        else:
            peasantScore *= (self.skill/10)
        if self.tech == 8:
            return peasantScore * 2
        elif self.tech == 7:
            return peasantScore * 1.75
        elif self.tech == 6:
            return peasantScore * 1.5
        elif self.tech == 5:
            return peasantScore * 1.25
        elif self.tech == 4:
            return peasantScore
        elif self.tech == 3:
            return peasantScore * .75
        elif self.tech == 2:
            return peasantScore * .5
        elif self.tech == 1:
            return peasantScore * .25
        elif self.tech == 0:
            return peasantScore * .1
class battleCalc:
    def __init__(self, offense, defense, elitePercent, troopPercent, peasantPercent, stakes, type, withdraw):
        ### Country
        self.offense = offense
        ### Country
        self.defense = defense
        ### Anywhere from 10% to 100% of a countries gold
        self.elitePercent = elitePercent
        self.troopPercent = troopPercent
        self.peasantPercent = peasantPercent
        self.stakes = stakes
        self.type = type
        self.withdraw = withdraw
    def invasion(self):
        offense = warscoreCalc(math.floor(self.offense.elite * self.elitePercent), math.ceil(self.offense.troop * self.troopPercent), math.ceil(self.offense.peasant * self.peasantPercent), 1, self.offense.tech)
        defense = warscoreCalc(math.ceil(self.defense.elite * .25), math.ceil(self.defense.troop/self.defense.land), math.ceil(self.defense.peasant/self.defense.land), 1, self.defense.tech)
        ### In order to be able to get losses and what not elites fight elites, soldiers fight soldiers, peasants fight peasants.
        ### If offense hits the withdraw percent they retreat
        ### Defense does not retreat
        phases = random.randrange(1, 20)
        ### Battles are divided into phases 
        ### At the start of each phase a check is done to see if the withdraw percent has been reached
        ### As well, some math is done to make some random modifications to the warscore of each side to keep things random
        ### At the end of each phase a 'dice roll' happens to see if there will be a random event or not
        ### During each phase more of each force face each other
