# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

# 

from scene import *
import ui
import time
import random
import globals
from sys import argv
import os

from main_menu_scene import *


class GamePick(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
                              
        self.newgame_button = (LabelNode(text = 'Continue Game',
                   position = self.size / 2,
                   parent = self,
                   scale = 1.25,
                   color = '#a50000',
                   font = ('CopperPlate-Light', 40)))
                   
    def update(self):
        #this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.newgame_button.frame.contains_point(touch.location):
            gamefile = 'game1'
            
            if os.path.isfile(gamefile) and os.access(gamefile, os.R_OK):
                game = open(gamefile, 'r')
                line = game.readline().rstrip('\n')
                myhealth = int(line)
                if myhealth > globals.fullhealth:
                    globals.fullhealth = myhealth
                line = game.readline().rstrip('\n')
                mydmglow = int(line)
                if mydmglow > globals.playerdmglowest:
                    globals.playerdmglowest = mydmglow
                line = game.readline().rstrip('\n')
                mydmghigh = int(line)
                if mydmghigh > globals.playerdmghighest:
                    globals.playerdmghighest = mydmghigh
                line = game.readline().rstrip('\n')
                mycritdmg = int(line)
                if mycritdmg > globals.playercritdmg:
                    globals.playercritdmg = mycritdmg
                line = game.readline().rstrip('\n')
                line = game.readline().rstrip('\n')
                line = game.readline().rstrip('\n')
                line = game.readline().rstrip('\n')
                line = game.readline().rstrip('\n')
                mycoins = int(line)
                if mycoins > globals.coins:
                    globals.coins = mycoins
                game.close()
            else:
                self.autosave(gamefile)
            
            self.present_modal_scene(MainMenuScene()) 
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
        
    def autosave(self, gamefile):
        tempfile = gamefile + '.tmp'
        game = open(tempfile, 'w')
        game.truncate()
        game.write(str(globals.fullhealth))
        game.write('\n')
        game.write(str(globals.playerdmglowest))
        game.write('\n')
        game.write(str(globals.playerdmghighest))
        game.write('\n')
        game.write(str(globals.playercritdmg))
        game.write('\n')
        game.write(str(globals.playercritchance))
        game.write('\n')
        game.write(str(globals.overtimeregen))
        game.write('\n')
        game.write(str(globals.playerarmor))
        game.write('\n')
        game.write(str(globals.playeratkspeed))
        game.write('\n')
        game.write(str(globals.coins))
        game.write('\n')
        game.close()
        os.rename(tempfile, gamefile)
