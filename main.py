from random import *
r = randint(1,5)
class Grandparents:
    speed = 1
    sick = 'coronary heart disease'
    height = 150
class Parents:
    height = 165
    speed = 5
class Child(Parents):
    speed = 8
    def __init__(self):
        print(self.sick)
        print(self.height)
        print(self.speed)
max_roma_pavlo = Grandparents()