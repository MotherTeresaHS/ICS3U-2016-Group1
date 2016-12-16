# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time

from main_menu_scene import *


class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.loadbar = []
        self.timee = 0
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
                                     
        self.game_label = LabelNode(text = 'HIT & RUN',
                                     font=('Markerfelt-Wide', 80),
                                     parent = self,
                                     position = self.size / 2,
                                     color = '#565656')
    def update(self):
        #this method is called, hopefully, 60 times a second
        self.bar = self.screen_center_y - 200
        self.fulltimee = 100
        self.loadmaxpixels = 400
        self.pixels = int(self.loadmaxpixels * self.timee / self.fulltimee)
        self.offset = int((self.loadmaxpixels - self.pixels) / 2)
        self.percent = int(self.timee * 100 / self.fulltimee)
        
        
       
        if self.timee == self.fulltimee or self.timee > 100:
           if not self.presented_scene and time.time() - self.start_time > 1.5:
            self.dismiss_modal_scene()
            self.present_modal_scene(MainMenuScene())
        else:
           self.timee = self.timee + random.randint(1,2)
           for loadingbar in self.loadbar:
                loadingbar.remove_from_parent()
                self.loadbar.remove(loadingbar)
           self.disloadbar()
           
    
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
    def disloadbar(self):
        
        self.loadbar.append((SpriteNode('./assets/sprites/health.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar + 69),
                              parent = self,
                              scale = 1,
                              size = (self.pixels, 42),
                              color = 'black')))
