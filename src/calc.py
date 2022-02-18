### Does some more complex calculations
### Most of said calculations will relate to things like warscore and shit
import random

class warscoreCalc:
    def __init__(self, elite, troop, peasant, skill, tech):
        self.elite = elite
        self.troop = troop
        self.peasant = peasant
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
