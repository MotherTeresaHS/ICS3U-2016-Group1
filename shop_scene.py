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



class HitAndRunShopScene(Scene):
    def setup(self):
        self.coinss = []
        self.heart = []
        self.heartshow = 1
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
                                     
        
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = (75, self.size_of_screen_y - 75),
                                       scale = 0.17,
                                       color = 'grey')
                                       
        self.backsquare1 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x, self.screen_center_y),
                                       scale = 0.55,
                                       color = 'grey')
                                       
        self.backsquare2 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x + 193, self.screen_center_y),
                                       scale = 0.55,
                                       color = 'grey')
        self.backsquare3 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x - 193, self.screen_center_y),
                                       scale = 0.55,
                                       color = 'grey')
        self.backsquare4 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x, self.screen_center_y - 289),
                                       scale = 0.55,
                                       color = 'grey')
                                       
        self.backsquare5 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x + 193, self.screen_center_y - 289),
                                       scale = 0.55,
                                       color = 'grey')
        self.backsquare6 = SpriteNode('assets/sprites/shop/shoptab.PNG',
                                       parent = self,
                                       position = (self.screen_center_x - 193, self.screen_center_y - 289),
                                       scale = 0.55,
                                       color = 'grey')
        
        self.heartback = SpriteNode('./assets/sprites/shop/frame-1.png',
                                     parent = self,
                                     scale = 0.12,
                                     position = (self.screen_center_x, self.screen_center_y + 5))
        
        self.hp_boost_label = LabelNode(text = 'HP BOOST',
                                     font=('CopperPlate-Light', 10),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y - 30),
                                     color = 'red')
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        
        # after 2 seconds, move to main menu scene
        for displaycoins in self.coinss:
            displaycoins.remove_from_parent()
            self.coinss.remove(displaycoins)
        self.coinss.append(LabelNode(text = 'Coins - ' + str(globals.coins),
                                     font = ('CopperPlate-Light', 30),
                                     parent = self,
                                     position = (self.screen_center_x, self.size_of_screen_y - 50),
                                     color = 'gold'))
        
        
        for heartshine in self.heart:
            heartshine.remove_from_parent()
            self.heart.remove(heartshine)
            self.heartshow = self.heartshow + 1
            time.sleep(0.08)
        if self.heartshow == 1:
            self.heart.append(SpriteNode('./assets/sprites/shop/frame-1.png',
                                     parent = self,
                                     scale = 0.12,
                                     position = (self.screen_center_x, self.screen_center_y + 5)))
                                     
        elif self.heartshow == 2:
            self.heart.append(SpriteNode('./assets/sprites/shop/frame-2.png',
                                     parent = self,
                                     scale = 0.12,
                                     position = (self.screen_center_x, self.screen_center_y + 5)))
        elif self.heartshow == 3:
            self.heart.append(SpriteNode('./assets/sprites/shop/frame-3.png',
                                     parent = self,
                                     scale = 0.12,
                                     position = (self.screen_center_x, self.screen_center_y + 5)))
        elif self.heartshow == 4:
            self.heart.append(SpriteNode('./assets/sprites/shop/frame-4.png',
                                     parent = self,
                                     scale = 0.12,
                                     position = (self.screen_center_x, self.screen_center_y + 5)))
        elif self.heartshow >= 5:
            self.heartshow = 1
        
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
        
    
                                     
    
        
