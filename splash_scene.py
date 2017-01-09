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


from gamepick import *


class SplashScene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        self.timee = 0
        self.loadbar = []
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/backgroundload.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'HIT & RUN',
                                    font=('CopperPlate-Bold', 80),
                                    parent = self,
                                    position = (self.screen_center_x, self.screen_center_y + 75),
                                    color = 'black')
                                     
        self.loadbarback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                              position = (self.screen_center_x, self.screen_center_y - 15),
                              parent = self,
                              scale = 1,
                              size = (380, 30)))
        self.loadbarright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                              position = (self.screen_center_x + 195, self.screen_center_y - 15),
                              parent = self,
                              scale = 1.25,
                              size = (10, 30)))
                              
        self.loadbarleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                              position = (self.screen_center_x - 195, self.screen_center_y - 15),
                              parent = self,
                              scale = 1.25,
                              size = (10, 30)))
        
        self.rightsword = (SpriteNode('./assets/sprites/splash/swords.PNG', 
                              position = (self.screen_center_x + 225, self.screen_center_y - 15),
                              parent = self,
                              color = 'black',
                              scale = 0.6))
                              
        
        self.leftsword = (SpriteNode('./assets/sprites/splash/swords.PNG', 
                              position = (self.screen_center_x - 225, self.screen_center_y - 15),
                              parent = self,
                              color = 'black',
                              scale = 0.6))
                              
        
    def update(self):
        #this method is called, hopefully, 60 times a second
        self.fulltimee = 380
        self.bar = self.screen_center_y - 15
        self.loadmaxpixels = 380
        self.pixels = self.loadmaxpixels * self.timee / self.fulltimee
        self.offset = (self.loadmaxpixels - self.pixels) / 2
        self.percent = (self.timee * 100) / self.fulltimee
        
        if self.pixels < 0:
            self.pixels = 0
                              
        if self.timee >= 380:
            if not self.presented_scene and time.time() - self.start_time > 3:
               self.dismiss_modal_scene()
               self.present_modal_scene(MainMenuScene())
        else:
           self.timee = self.timee + random.randint(2,2)
           for loadingbar in self.loadbar:
                loadingbar.remove_from_parent()
                self.loadbar.remove(loadingbar)
        
        
        self.loadbar.append(SpriteNode('./assets/sprites/splash/loadbar.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar),
                              parent = self,
                              size = (self.pixels, 25)))
                              
        if self.percent <= 30:
            self.loadbar.append(LabelNode(text = str(self.percent) + '%',
                                      position = (self.screen_center_x, self.bar),
                                      color = '#ff0000',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
        elif self.percent <= 80 and self.percent > 30:
            self.loadbar.append(LabelNode(text = str(self.percent) + '%',
                                      position = (self.screen_center_x, self.bar),
                                      color = '#faca1d',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
        else:
            self.loadbar.append(LabelNode(text = str(self.percent) + '%',
                                      position = (self.screen_center_x, self.bar),
                                      color = '#00f215',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
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
