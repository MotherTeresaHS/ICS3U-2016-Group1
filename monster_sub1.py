#made by kyle
#made in dec 2016
#made for ics3u
#this is the class for monsters

from monster import *
from scene import *

class Orc(Monster):
    
    def __init__(self):
        self.__damage_orc = 20
        self.__health_orc = 50
        self.__speed_orc = 35
    
    @property
    def orc_damage(self):
        return self.__damage_orc
    @orc_damage.setter
    def orc_damage(self):
        self.__damage_orc = new_orc_dmg
        
    @property
    def orc_health(self):
        return self.__health_orc
    @orc_health.setter
    def orc_health(self):
        self.__health_orc = new_orc_hp
        
    @property
    def orc_speed(self):
        return self.__speed_orc
    @orc_speed.setter
    def orc_speed(self):
        self.__speed_orc = new_orc_spd
