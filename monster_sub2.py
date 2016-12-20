#made by kyle
#made in dec 2016
#made for ics3u
#this is the class for monsters

from monster import *
from scene import *

class Troll(Monster):
    
    def __init__(self):
        self.__damage_troll = 15
        self.__health_troll = 100
        self.__speed_troll = 35
    
    @property
    def troll_damage(self):
        return self.__damage_troll
    @troll_damage.setter
    def troll_damage(self):
        self.__damage_troll = new_troll_dmg
        
    @property
    def troll_health(self):
        return self.__health_troll
    @troll_health.setter
    def troll_health(self):
        self.__health_troll = new_troll_hp
        
    @property
    def troll_speed(self):
        return self.__speed_troll
    @troll_speed.setter
    def troll_speed(self):
        self.__speed_troll = new_troll_spd
