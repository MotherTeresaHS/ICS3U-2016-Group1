from scene import *

import time
import ui
import random

import globals
from game_scene_pause import *


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.currentstate = 'stand'
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        self.healthbar = []
        self.charater = []
        self.pathsprites = []
        self.pathnames = []
        self.pathy = []
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        self.yvalue = 0
        self.pathrange = int(self.size_of_screen_y / 222 +1) +1
        #print(str(len(self.pathsprites)) + ' : ' + str(self.pathrange))
        
        for roadpiece in range(self.pathrange):
            self.pathnames.append('./assets/sprites/game/road.JPG')
            self.pathy.append(self.yvalue)
            #self.pathsprites.append(SpriteNode(self.pathnames[roadpiece],
             #                                  position = (self.screen_center_x, self.pathy[roadpiece]),
               #                                parent = self))
           # print(str(len(self.pathsprites)) + ' : ' + str(self.pathrange))
            self.yvalue = self.yvalue + 222
            
            
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size,
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
                              
        #self.fight = LabelNode(text = 'fight',
             #                 position = (self.screen_center_x, self.screen_center_y),
              #                parent = self)
                              
        #self.stand = LabelNode(text = 'stand',
       #                       position = (self.screen_center_x + 100, self.screen_center_y),
          #                    parent = self)
        #self.run = LabelNode(text = 'run',
           #                   position = (self.screen_center_x - 100, self.screen_center_y),
             #                 parent = self)
        
        self.health = globals.fullhealth
        self.rotationc = 1
    def update(self):
        # this method is called, hopefully, 60 times a second
        # after 2 seconds, move to main menu scene
        
        for roadp in self.pathsprites:
                roadp.remove_from_parent()
                self.pathsprites.remove(roadp)
        for roadp in self.pathsprites:
                roadp.remove_from_parent()
                self.pathsprites.remove(roadp)
        print (len(self.pathsprites))
        
        for roadpiece in range(self.pathrange):
            self.pathy[roadpiece] = self.pathy[roadpiece] - 4
            if self.pathy[roadpiece] < -111:
                self.pathy[roadpiece] = self.pathrange * 222 - 112
                self.pathnames[roadpiece] = './assets/sprites/game/road.JPG'
            #print(str(roadpiece) + ' ' + str(self.pathy[roadpiece]))
            self.pathsprites.append(SpriteNode(self.pathnames[roadpiece],
                                               position = (self.screen_center_x, self.pathy[roadpiece]),
                                               parent = self))
            
        print (len(self.pathsprites))
        
        for hpbar in self.healthbar:
                hpbar.remove_from_parent()
                self.healthbar.remove(hpbar)
        self.bar = 250
        self.healthmaxpixels = 300
        self.pixels = self.healthmaxpixels * globals.fullhealth / globals.fullhealth
        self.offset = (self.healthmaxpixels - self.pixels) / 2
        self.percent = globals.fullhealth * 100 / globals.fullhealth
        
        self.healthbar.append(SpriteNode('./assets/sprites/game/health.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar),
                              parent = self,
                              scale = 1.25,
                              size = (self.pixels, 25)))
        self.healthbar.append(LabelNode(text = '[' + str(self.health) + ' | ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%',
                                      position = (self.screen_center_x - self.offset, self.bar + 2),
                                      color = '#000000',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
        
        for movement in self.charater:
            movement.remove_from_parent()
            self.charater.remove(movement)
            #time.sleep(0.19)
        
        if self.rotationc == 1 and self.currentstate == 'run':
            self.charater.append(SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
            self.rotationc = self.rotationc + 1
        elif self.rotationc == 1 and self.currentstate == 'stand':
            rotationc = 1
            self.charater.append(SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
            
        elif self.rotationc == 2 and self.currentstate == 'run':
            self.charater.append(SpriteNode('./assets/sprites/game/rightstepguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
            self.rotationc = self.rotationc + 1
        elif self.rotationc == 3 and self.currentstate == 'run':
            self.charater.append(SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
            self.rotationc = self.rotationc + 1
        elif self.rotationc == 4 and self.currentstate == 'run':
            self.charater.append(SpriteNode('./assets/sprites/game/leftstepguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
            self.rotationc = self.rotationc + 1
        elif self.rotationc == 5 and self.currentstate == 'run':
            self.rotationc = 1
            self.charater.append(SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = 0.5,
                                     parent = self))
        
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
       # if self.stand.frame.contains_point(touch.location):
      #      self.currentstate = 'stand'
       #     self.rotationc = 1
        #if self.fight.frame.contains_point(touch.location):
         #   self.currentstate = 'fight'
       # if self.run.frame.contains_point(touch.location):
          #  self.currentstate = 'run'
        #    self.rotationc = 1
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
        
        
    #def screenscroll(self):
        # add a new alien to come down
        
        
