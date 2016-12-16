from scene import *

import time
import ui

import globals 
import stats_scene 
import credits_scene 
import shop_scene 
import help_scene 
import game_scene 
import settings_scene 
from game_scene_pause import *


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        self.healthbar = []
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.pause_button = SpriteNode('assets/sprites/game/pause.PNG',
                                       parent = self,
                                       position = (self.size_of_screen_x - 75, self.size_of_screen_y - 75),
                                       scale = 0.17,
                                       color = 'grey')
        
        self.loadbarback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                              position = (self.screen_center_x, self.screen_center_y - 460),
                              parent = self,
                              scale = 1.25,
                              size = (300, 30)))
        self.loadbarright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                              position = (self.screen_center_x + 195, self.screen_center_y - 460),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
                              
        self.loadbarleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                              position = (self.screen_center_x - 195, self.screen_center_y - 460),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        # after 2 seconds, move to main menu scene
        

        for hpbar in self.healthbar:
                hpbar.remove_from_parent()
                self.healthbar.remove(hpbar)
        self.dishealthbar()
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScenePause())
    
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
        
        
    def dishealthbar(self):
        self.bar = self.screen_center_y - 460
        self.healthmaxpixels = 300
        self.pixels = int(self.healthmaxpixels * globals.fullhealth / globals.fullhealth)
        self.offset = int((self.healthmaxpixels - self.pixels) / 2)
        self.percent = int(globals.fullhealth * 100 / globals.fullhealth)
        
        self.healthbar.append((SpriteNode('./assets/sprites/game/health.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar),
                              parent = self,
                              scale = 1.25,
                              size = (self.pixels, 25))))
                              
    
