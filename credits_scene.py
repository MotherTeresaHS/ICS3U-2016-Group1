from scene import *

import time
import ui

from main_menu_scene import *

class CreditsScene(Scene):
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
                                     size = self.size,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'Credits',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 70, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = back_button_position.y - 75
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.17,
                                       color = 'grey')
                                       
        self.credits_text = LabelNode(text = 'Made by Tristan A. Justin D. and Kyle B.\nImages from ... and created by Justin D.\nMade in Mr. Coxalls class\nGame Scene, Stats, Globals made by Tristan A.\nShop Scene, Sprites, Gifs made by Justin D.\nClasses, Credits, Help, Settings made by Kyle B.',
                                      font = ('Markerfelt-Wide', 30),
                                      parent = self,
                                      position = (self.size_of_screen_x - 384, self.size_of_screen_y - 512),
                                      color = '#d92e2e')
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
        if self.back_button.frame.contains_point(touch.location):
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
    
