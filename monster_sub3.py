#made by kyle
#made in dec 2016
#made for ics3u
#this is the class for monsters

from monster import *
from scene import *

class Goblin(Monster):
    
    def __init__(self):
        self.__damage_goblin = 10
        self.__health_goblin = 35
        self.__speed_goblin = 15
    
    @property
    def troll_damage(self):
        return self.__damage_goblin
    @goblin_damage.setter
    def troll_damage(self):
        self.__damage_goblin = new_goblin_dmg
        
    @property
    def goblin_health(self):
        return self.__health_goblin
    @goblin_health.setter
    def goblin_health(self):
        self.__health_goblin = new_goblin_hp
        
    @property
    def goblin_speed(self):
        return self.__speed_goblin
    @goblin_speed.setter
    def goblin_speed(self):
        self.__speed_goblin = new_goblin_spd
