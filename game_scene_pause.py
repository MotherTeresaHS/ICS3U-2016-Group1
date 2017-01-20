from scene import *

import time
import ui

from main_menu_scene import *
from game_scene import *

class GameScenePause(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.pausebackground = (SpriteNode(position = self.size / 2,
                   size = (self.size_of_screen_x, self.size_of_screen_y),
                   parent = self,
                   scale = 1.25,
                   color = '#ffffff',
                   alpha = 0.4))
                   
        self.resume_button = (LabelNode(text = 'Resume',
                   position = self.size / 2,
                   parent = self,
                   scale = 1.25,
                   color = '#a50000',
                   font = ('CopperPlate-Light', 40)))
                                       
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # after 2 seconds, move to main menu scene
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.resume_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
    
