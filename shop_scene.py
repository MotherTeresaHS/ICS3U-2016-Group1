from scene import *

import time
import ui

from main_menu_scene import *

class HitAndRunShopScene(Scene):
    def __init__(self):
        self.__coins = 100
        self.__fullhealth = 100
        self.__playerdmglowest = 50
        self.__playerdmghighest = 75
        self.__playercritchance = 5.25
        self.__playercritdmglowest = self.__playerdmglowest * 2
        self.__playercritdmghighest = self.__playerdmghighest * 2
        self.__overtimeregen = 5
        self.__playerarmor = 1.25
        self.__playeratkspeed = 1
    def setup(self):
        self.fixed_time_step = 'Nill'
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode('assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'Shop',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 50, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        self.coins_label = LabelNode(text = 'Coins - ' + str(self.__coins),
                                     font=('CopperPlate-Light', 30),
                                     parent = self,
                                     position = (self.screen_center_x, self.size_of_screen_y - 50),
                                     color = 'gold')
        
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = (75, self.size_of_screen_y - 75),
                                       scale = 0.17,
                                       color = 'grey')
                                       
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        # after 2 seconds, move to main menu scene
    
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
        
    def get_fullhealth(self):
        return self.__fullhealth
    
    def get_playerdmglowest(self):
        return self.__playerdmglowest
        
    def get_playerdmghighest(self):
        return self.__playerdmghighest
        
    def get_playercritchance(self):
        return self.__playercritchance
        
    def get_playercritdmglowest(self):
        return self.__playercritdmglowest
    
    def get_playercritdmghighest(self):
        return self.__playercritdmghighest
        
    def get_overtimeregen(self):
        return self.__overtimeregen
    
    def get_playerarmor(self):
        return self.__playerarmor
        
    def get_playeratkspeed(self):
        return self.__playeratkspeed
    
    def get_coins(self):
        return self.__coins
