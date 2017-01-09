from scene import *

import time
import ui
import random

import globals
from game_scene_pause import *


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.currentkills = 0
        self.currentround = 1
        self.currentcoins = 0
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        self.hud = []
        self.bard = []
        self.monsters = []
        self.dmglabels = []
        self.monster_attack_speed = 20.0
        self.monster_attack_rate = 5.0
        self.health = globals.fullhealth
        #CharaterStuff
        self.characterscale = 1.4
        self.characterpos = Vector2(self.screen_center_x, 200)
        self.charater = []
        self.rotationc = 0
        self.runspeed = 1
        self.swingspeed = 1
        self.timerdmglabel = 0
        #---------------------------------
        self.start_time = time.time()
        
        self.background = SpriteNode('./assets/sprites/game/roadtile.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size,
                                     scale = 2)
                                     
        
        
        self.pause_button = SpriteNode('assets/sprites/game/pause.PNG',
                                       parent = self,
                                       position = (self.size_of_screen_x - 75, self.size_of_screen_y - 75),
                                       scale = 0.17,
                                       color = '#c5c5c5')
        self.hit_button = SpriteNode(position = (self.screen_center_x + 200, self.screen_center_y - 200),
                   size = (self.size_of_screen_x, self.size_of_screen_y),
                   parent = self,
                   scale = 1.25,
                   color = '#bababa',
                   alpha = 0.0)
        self.interact_monsters = SpriteNode(position = (self.screen_center_x, 280),
                   size = (200, 50),
                   parent = self,
                   scale = 1,
                   color = '#bababa',
                   alpha = 0.0)
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.hit_button.frame.contains_point(touch.location):
            globals.currentstate = 'attack'
            self.rotationc = 1 
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScenePause())
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        # after 2 seconds, move to main menu scene
        
        #MonsterSpawn
        monster_create_chance = random.randint(1, 120)
        if monster_create_chance <= self.monster_attack_rate:
            self.add_monster()
        

        
        
        
        #Hud
        for huds in self.hud:
                huds.remove_from_parent()
                self.hud.remove(huds)
        
        for barc in self.bard:
                barc.remove_from_parent()
                self.bard.remove(barc)
        
        self.fullhp = globals.fullhealth
        self.bar = 50
        self.healthmaxpixels = 300
        self.pixels = int(self.healthmaxpixels * self.health / self.fullhp)
        self.offset = int((self.healthmaxpixels - self.pixels) / 2)
        self.percent = (self.health * 100) / self.fullhp
        
       
        self.bartop = self.size_of_screen_y - 50
        
        self.soulpixels = self.healthmaxpixels * globals.fullhealth / globals.fullhealth
        
        self.souloffset = (self.healthmaxpixels - self.soulpixels) / 2
        
        #print('HP= ' + str(self.health) + ' / ' + str(globals.fullhealth) + ' : PX= ' + str(self.healthmaxpixels) + ' - ' + str(self.pixels) + ' = ' + str((self.healthmaxpixels - self.pixels)) + ' : Pos= ' + str(self.screen_center_x) + ' - ' + str(self.offset) + ' = ' + str((self.screen_center_x - self.offset)) + ' (' + str((self.screen_center_x - self.offset - (self.pixels /2))) + '-' + str((self.screen_center_x - self.offset + (self.pixels /2))) + ')')
        
        
        self.hud.append(SpriteNode('./assets/sprites/game/emptybar.JPG', 
                              position = (self.screen_center_x, self.bar),
                              parent = self,
                              scale = 1.25,
                              size = (300, 30)))
        self.hud.append(SpriteNode('./assets/sprites/game/barright.PNG', 
                              position = (self.screen_center_x + 195, self.bar),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
                              
        self.hud.append(SpriteNode('./assets/sprites/game/barleft.PNG', 
                              position = (self.screen_center_x - 195, self.bar),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
                              
        self.bard.append(SpriteNode('./assets/sprites/game/health.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar),
                              parent = self,
                              scale = 1.25,
                              color = '#cbbcbc',
                              size = (self.pixels, 25)))
                              
        self.hud.append(LabelNode(text = '[' + str(self.health) + ' | ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%',
                                      position = (self.screen_center_x, 52),
                                      color = '#000000',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
                                      
        self.hud.append(SpriteNode('./assets/sprites/game/gamestats.PNG', 
                              position = (self.screen_center_x, self.bartop - 50),
                              parent = self,
                              scale = 1))
                              
        
        self.hud.append(LabelNode(text = 'Kills ' + str(self.currentkills),
                                    font=('CopperPlate-Bold', 20),
                                    parent = self,
                                    position = (self.screen_center_x, self.size_of_screen_y - 90),
                                    color = '#d2a710'))
                                    
        self.hud.append(LabelNode(text = 'Coins ' + str(self.currentcoins),
                                    font=('CopperPlate-Bold', 20),
                                    parent = self,
                                    position = (self.screen_center_x, self.size_of_screen_y - 110),
                                    color = '#d2a710'))
                                    
        self.hud.append(SpriteNode('./assets/sprites/game/emptybar.JPG', 
                              position = (self.screen_center_x, self.bartop),
                              parent = self,
                              scale = 1.25,
                              size = (300, 30)))
        self.hud.append(SpriteNode('./assets/sprites/game/barright.PNG', 
                              position = (self.screen_center_x + 195, self.bartop),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
                              
        self.hud.append(SpriteNode('./assets/sprites/game/barleft.PNG', 
                              position = (self.screen_center_x - 195, self.bartop),
                              parent = self,
                              scale = 1.25,
                              size = (15, 38)))
        
        self.bard.append(SpriteNode('./assets/sprites/splash/loadbar.PNG', 
                              position = (self.screen_center_x - self.souloffset, self.bartop),
                              parent = self,
                              scale = 1.25,
                              color = '#5effea',
                              size = (self.soulpixels, 25)))
        
        self.hud.append(LabelNode(text = 'Round ' + str(self.currentround),
                                    font=('CopperPlate-Bold', 20),
                                    parent = self,
                                    position = (self.screen_center_x, self.bartop + 5),
                                    color = '#000000'))
                                    
        
        
        #CharaterActions
        
        
        for movement in self.charater:
            movement.remove_from_parent()
            self.charater.remove(movement)
            
        if globals.currentstate == 'attack':
            if self.rotationc <= self.swingspeed:
                self.charater.append(SpriteNode('./assets/sprites/game/swing1.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
                                     
            elif self.rotationc > self.swingspeed and self.rotationc <= (self.swingspeed * 2):
                self.charater.append(SpriteNode('./assets/sprites/game/swing2.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.swingspeed * 2) and self.rotationc <= (self.swingspeed * 3):
                self.charater.append(SpriteNode('./assets/sprites/game/swing3.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.swingspeed * 3) and self.rotationc <= (self.swingspeed * 4):
                self.charater.append(SpriteNode('./assets/sprites/game/swing4.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.swingspeed * 4) and self.rotationc <= (self.swingspeed * 5):
                self.charater.append(SpriteNode('./assets/sprites/game/swing5.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.swingspeed * 5) and self.rotationc <= (self.swingspeed * 6):
                self.charater.append(SpriteNode('./assets/sprites/game/swing6.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.swingspeed * 6):
                self.charater.append(SpriteNode('./assets/sprites/game/swing6.PNG',
                                     position = (self.screen_center_x, 207),
                                     scale = self.characterscale,
                                     parent = self))
                globals.currentstate = 'run'
                self.rotationc = 1
                
        elif globals.currentstate == 'run':
            
            if self.rotationc <= self.runspeed:
                self.charater.append(SpriteNode('./assets/sprites/game/step1.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
                                     
            elif self.rotationc > self.runspeed and self.rotationc <= (self.runspeed * 2):
                self.charater.append(SpriteNode('./assets/sprites/game/step2.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 2) and self.rotationc <= (self.runspeed * 3):
                self.charater.append(SpriteNode('./assets/sprites/game/step3.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 3) and self.rotationc <= (self.runspeed * 4):
                self.charater.append(SpriteNode('./assets/sprites/game/step4.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 4) and self.rotationc <= (self.runspeed * 5):
                self.charater.append(SpriteNode('./assets/sprites/game/step5.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 5) and self.rotationc <= (self.runspeed * 6):
                self.charater.append(SpriteNode('./assets/sprites/game/step6.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 6) and self.rotationc <= (self.runspeed * 7):
                self.charater.append(SpriteNode('./assets/sprites/game/step7.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 7) and self.rotationc <= (self.runspeed * 8):
                self.charater.append(SpriteNode('./assets/sprites/game/step8.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
            
            elif self.rotationc > (self.runspeed * 8):
                self.charater.append(SpriteNode('./assets/sprites/game/step8.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
                self.rotationc = 0
                
            
        elif globals.currentstate == 'stand':
            self.charater.append(SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                     position = (self.screen_center_x, 200),
                                     scale = self.characterscale,
                                     parent = self))
        
        if self.timerdmglabel >= 10:
            self.timerdmglabel = 0
            for dmglabel in self.dmglabels:
                dmglabel.remove_from_parent()
                self.dmglabels.remove(dmglabel)
                
        self.rotationc = self.rotationc + 1
        self.timerdmglabel = self.timerdmglabel + 1
        for monster in self.monsters:
            if monster.frame.intersects(self.interact_monsters.frame) or monster.position.y == 280:
                if globals.currentstate == 'attack' and self.rotationc == 5:
                    self.dmglabels.append(LabelNode(text = str(random.randint(globals.playerdmglowest, globals.playerdmghighest)),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 300 + random.randint(1, 25) - random.randint(1, 25)),
                                      color = '#ac0000',
                                      font = ('AvenirNext-Heavy', 25),
                                      parent = self))
                    monster.remove_from_parent()
                    self.monsters.remove(monster)
                    self.currentkills = self.currentkills + 1
                    self.currentcoins = self.currentcoins + random.randint(3,10)
                    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
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
        
        
    #def screenscroll(self):
        # add a new alien to come down
        
    def add_monster(self):
        # add a new alien to come down
        
        monster_start_position = Vector2()
        monster_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        monster_start_position.y = self.size_of_screen_y + 100
        
        monster_end_position = Vector2()
        monster_end_position.x = self.screen_center_x - 50 + random.randint(0, 100)
        monster_end_position.y = 280
        
        self.monsters.append(SpriteNode('./assets/sprites/game/straightreaper.PNG',
                             position = monster_start_position,
                             parent = self))
        
                             
        # make missile move forward
        monsterMoveAction = Action.move_to(monster_end_position.x, 
                                         monster_end_position.y, 
                                         self.monster_attack_speed,
                                         TIMING_SINODIAL)
        self.monsters[len(self.monsters)-1].run_action(monsterMoveAction)
