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

class StatsScene(Scene):
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
                                     position = (self.screen_center_x, self.screen_center_y),
                                     parent = self,
                                     scale = 1.25)
                                     
        
                                     
        self.game_label = LabelNode(text = 'Stats',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 55, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        self.health_label = LabelNode(text = 'HEALTH',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (110, self.size_of_screen_y - 400),
                                     color = 'grey')
                                     
                                     
                                     
        self.playerdmg_label = LabelNode(text = 'DAMAGE',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (114, self.size_of_screen_y - 200),
                                     color = 'grey')
                                     
        self.playercritdmg_label = LabelNode(text = 'CRIT DAMAGE',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (169, self.size_of_screen_y - 250),
                                     color = 'grey')
                                     
        self.playercritchance_label = LabelNode(text = 'CRIT CHANCE',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (170, self.size_of_screen_y - 300),
                                     color = 'grey')
                                     
        self.playerselfregen_label = LabelNode(text = 'REGEN',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (100, self.size_of_screen_y - 350),
                                     color = 'grey')
                                     
        self.playerarmor_label = LabelNode(text = 'ARMOR',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (102, self.size_of_screen_y - 450),
                                     color = 'grey')
                                     
        self.playeratkspeed_label = LabelNode(text = 'ATTACK CD',
                                     font=('CopperPlate-Light', 40),
                                     parent = self,
                                     position = (141, self.size_of_screen_y - 500),
                                     color = 'grey')
                                     
        self.health_label = LabelNode(text = str(globals.fullhealth) + 'hp',
                            font = ('CopperPlate-Light', 20),
                            parent = self,
                            position = (self.screen_center_x+100, self.size_of_screen_y - 400),
                            color = '#d40000')
                                     
                                     
                                     
        self.playerdmg_label = LabelNode(text = str(globals.playerdmglowest) + '-' + str(globals.playerdmghighest) + 'dmg',
                                         font = ('CopperPlate-Light', 20),
                                         parent = self,
                                         position = (self.screen_center_x + 100, self.size_of_screen_y - 200),
                                         color = '#32cce3')
                                     
        self.playercritdmg_label = LabelNode(text = str(globals.playercritdmglowest) + '-' + str(globals.playercritdmghighest) + 'dmg',
                                   font = ('CopperPlate-Light', 20),
                                   parent = self,
                                   position = (self.screen_center_x + 100, self.size_of_screen_y - 250),
                                   color = '#7f00b8')
                                     
        self.playercritchance_label = LabelNode(text = str(globals.playercritchance) + '%',
                                      font = ('CopperPlate-Light', 20),
                                      parent = self,
                                      position = (self.screen_center_x + 100, self.size_of_screen_y - 300),
                                      color = '#c66d0b')
                                     
        self.playerselfregen_label = LabelNode(text = str(globals.overtimeregen) + 'hp /5s',
                                     font=('CopperPlate-Light', 20),
                                     parent = self,
                                     position = (self.screen_center_x + 100, self.size_of_screen_y - 350),
                                     color = '#28e400')
                                     
        self.playerarmor_label = LabelNode(text = str(globals.playerarmor) + '%',
                                     font=('CopperPlate-Light', 20),
                                     parent = self,
                                     position = (self.screen_center_x + 100, self.size_of_screen_y - 450),
                                     color = '#cbcbcb')
                                     
        self.playeratkspeed_label = LabelNode(text = str(globals.playeratkspeed) + 's',
                                     font=('CopperPlate-Light', 20),
                                     parent = self,
                                     position = (self.screen_center_x + 100, self.size_of_screen_y - 500),
                                     color = '#ffd028')
                                     
        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = back_button_position.y - 75
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.17,
                                       color = 'grey')
                                       
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
