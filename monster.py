#made by kyle
#made in dec 2016
#made for ics3u
#this is the class for monsters

from scene import *

class Monster:
    
    def __init__(self):
        self.__monster_orc = ui.Image('assets/scenes/monsters/Orc.png')
        self.__monster_troll = ui.Image('assets/scenes/monsters/Troll.png')
        self.__monster_goblin = ui.Image('assets/scenes/monsters/Goblin.png')
        
    def get_monster_orc(self):
        return self.__monster_orc
    def get_monster_troll(self):
        return self.__monster_troll
    def get_monster_goblin(self):
        return self.__monster_goblin
