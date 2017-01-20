from scene import *

import time
import ui
import random

import globals
from game_scene_pause import *


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        #Positions and defaults
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        #Stats and counters
        self.currentkills = 0
        self.currentround = 1
        self.currentcoins = 0
        self.runspeed = 2
        self.swingspeed = 1.4
        self.currentarmor = 50
        self.currentatk = 0.5
        self.currentroundkills = 0
        self.state = globals.currentstate
        self.monsterspawned = 0
        self.monsterattack = 0
        self.timerregen = 0
        self.rotationc = 0
        self.timerdmglabel = 0
        self.timerroundup = 0
        self.health = globals.fullhealth
        self.fullhp = globals.fullhealth
        self.roundkills = self.currentround * 4
        self.monster_attack_speed = 20.0
        self.monster_attack_rate = 5.0
        self.armor = globals.playerarmor
        self.timerblock = 0
        self.crit = globals.playercritchance
        self.stopwatch = 0
        #Lists
        self.monsters = []
        self.dmglabels = []
        self.roundup = []
        self.regenover5 = []
        self.blocklabels = []
        self.dead = []
        self.dea = 0
        #Times
        self.currenttimeh = time.time()
        self.regentime = time.time()
        #CharaterStuff
        self.characterscale = 1.4
        self.characterpos = Vector2(self.screen_center_x, 200)
        #Bars
        self.bar = 25
        self.healthmaxpixels = 300
        self.pixels = int(self.healthmaxpixels * self.health / self.fullhp)
        self.percent = (self.health * 100) / self.fullhp
        #---------------------------------
        self.soulmaxpixels = 300
        self.sbar = 50
        self.soulpixels = self.soulmaxpixels * self.currentroundkills / self.roundkills
        #---------------------------------
        self.fullatk = globals.playeratkspeed
        self.attackmaxpixels = 300
        self.atbar = self.size_of_screen_x - 50
        self.waitattack = time.time()
        self.attackpixels = min((1 - (self.waitattack - self.currenttimeh) / self.fullatk), 1) * self.attackmaxpixels
        #---------------------------------
        self.armormaxpixels = 300
        self.arbar = 60
        self.armorpixels = self.armormaxpixels * self.currentarmor / 50
        #Image and Label Setups
        self.background = SpriteNode('./assets/sprites/game/roadtile.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size,
                                     scale = 2)
        
        self.attackback = (SpriteNode('./assets/sprites/game/updownpipe.PNG', 
                                      position = (self.atbar, 300),
                                      parent = self,
                                      scale = 1,
                                      size = (20, 300)))
        self.attackright = (SpriteNode('./assets/sprites/game/updowntop.PNG', 
                                       position = (self.atbar, 457),
                                       parent = self,
                                       scale = 1.25,
                                       size = (20, 15)))
        self.attackleft = (SpriteNode('./assets/sprites/game/updownbottom.PNG', 
                                      position = (self.atbar, 143),
                                      parent = self,
                                      scale = 1.25,
                                      size = (20, 15)))
        self.attackbar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                     position = (self.atbar, 150),
                                     parent = self,
                                     scale = 1,
                                     anchor_point = (0.5, 0),
                                     color = '#ce5eff',
                                     size = (20, self.attackpixels)))
        self.armorback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                                     position = (self.screen_center_x, self.arbar),
                                     parent = self,
                                     scale = 1,
                                     size = (self.armormaxpixels, 20)))
        self.armorright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                                      position = (self.screen_center_x + 157, self.arbar),
                                      parent = self,
                                      scale = 1.25,
                                      size = (15, 20)))
        self.armorleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                                     position = (self.screen_center_x - 157, self.arbar),
                                     parent = self,
                                     scale = 1.25,
                                     size = (15, 20)))
        self.armorbar = (SpriteNode('./assets/sprites/splash/loadbar.PNG', 
                                    position = (self.screen_center_x - 150, self.arbar),
                                    parent = self,
                                    anchor_point = (0, 0.5),
                                    scale = 1,
                                    color = '#e6dada',
                                    size = (self.armorpixels, 20)))
        self.hpback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                                  position = (self.screen_center_x, self.bar),
                                  parent = self,
                                  scale = 1.25,
                                  size = (300, 30)))
        self.hpright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                                   position = (self.screen_center_x + 195, self.bar),
                                   parent = self,
                                   scale = 1.25,
                                   size = (15, 38)))
        self.hpleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                                  position = (self.screen_center_x - 195, self.bar),
                                  parent = self,
                                  scale = 1.25,
                                  size = (15, 38)))
        self.hpbar = (SpriteNode('./assets/sprites/game/health.PNG', 
                                 position = (self.screen_center_x - 187, self.bar),
                                 parent = self,
                                 scale = 1.25,
                                 color = '#cbbcbc',
                                 anchor_point = (0, 0.5),
                                 size = (self.pixels, 28)))
        self.hplabel = (LabelNode(text = '[' + str(self.health) + ' / ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%',
                                  position = (self.screen_center_x, self.bar + 2),
                                  color = '#000000',
                                  font = ('CopperPlate-Bold', 18),
                                  parent = self))
        
        self.timelabel = (LabelNode(text = str(self.stopwatch) + 's',
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#e2e2e2',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 40)))
                                     
        self.timer_img = SpriteNode('assets/sprites/timer.PNG', 
                                     position = (self.sbar, self.screen_center_y + 40),
                                     parent = self,
                                     color = '#ffffff',
                                     scale = 0.13)
        
        self.killslabel = (LabelNode(text = str(self.currentkills),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#000000',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 90)))
                                     
        self.skull_img = SpriteNode('assets/sprites/skull.PNG', 
                                     position = (self.sbar, self.screen_center_y + 90),
                                     parent = self,
                                     scale = 0.11)
                                     
        self.coinslabel = (LabelNode(text = str(self.currentcoins),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = 'gold',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 140)))
                                     
        self.coins_img = SpriteNode('assets/sprites/coins.PNG', 
                                     position = (self.sbar, self.screen_center_y + 140),
                                     parent = self,
                                     scale = 0.06)
                                     
        self.soulbarback = (SpriteNode('./assets/sprites/game/updownpipe.PNG', 
                                       position = (self.sbar, 300),
                                       parent = self,
                                       scale = 1,
                                       size = (20, 300)))
        self.soulbarright = (SpriteNode('./assets/sprites/game/updowntop.PNG', 
                                        position = (self.sbar, 457),
                                        parent = self,
                                        scale = 1.25,
                                        size = (20, 15)))
        self.soulbarleft = (SpriteNode('./assets/sprites/game/updownbottom.PNG', 
                                       position = (self.sbar, 143),
                                       parent = self,
                                       scale = 1.25,
                                       size = (20, 15)))
        self.soulbar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                   position = (self.sbar, 150),
                                   parent = self,
                                   scale = 1,
                                   anchor_point = (0.5, 0),
                                   color = '#5effea',
                                   size = (20, self.soulpixels)))
        self.charater = (SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                    position = (self.screen_center_x, 200),
                                    scale = self.characterscale,
                                    parent = self))
        
        self.hit_button = SpriteNode(position = (self.size_of_screen_x - 300, 0 + 5),
                   anchor_point = (0.5, 0),
                   size = (self.size_of_screen_x - 300, self.size_of_screen_y -  300),
                   parent = self,
                   scale = 1.25,
                   color = '#bababa',
                   alpha = 0.0)
        self.runtime = time.time()
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.hit_button.frame.contains_point(touch.location) and self.health != globals.fullhealth + 1:
           if self.waitattack < time.time():
                self.state = 'attack'
                self.rotationc = 1 
        if self.health == globals.fullhealth + 1:
            if self.dead.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.pixels = self.healthmaxpixels * self.health / self.fullhp
        self.percent = int(round((self.health * 100) / self.fullhp))
        #---------------------------------
        self.soulpixels = self.soulmaxpixels * self.currentroundkills / self.roundkills
        #---------------------------------
        self.currenttimeh = time.time()
        self.attackpixels = min((1 - (self.waitattack - self.currenttimeh) / self.fullatk), 1) * self.attackmaxpixels
        #---------------------------------
        self.armorpixels = self.armormaxpixels * self.currentarmor / 50
        self.coinslabel.text = str(self.currentcoins)
        self.killslabel.text = str(self.currentkills)
        self.soulbar.size = (20, self.soulpixels)
        self.armorbar.size = (self.armorpixels, 20)
        self.hpbar.size = (self.pixels, 28)
        self.attackbar.size = (20, self.attackpixels)
        self.hplabel.text = '[' + str(self.health) + ' / ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%'
        
        self.timerroundup = self.timerroundup + 1
        self.timerblock = self.timerblock + 1
        self.rotationc = self.rotationc + 1
        self.monsterattack = self.monsterattack + 1
        self.timerregen = self.timerregen + 1
        
        if self.dea == 0:
            self.timelabel.text = str((int(time.time() - self.runtime) * 100) / 100) + 's'
        
        if self.health <= 0:
            self.health = globals.fullhealth + 1
            self.state = 'dead'
            for monster in self.monsters:
                monster.remove_from_parent()
                self.monsters.remove(monster)
            globals.coins = globals.coins + self.currentcoins
            self.removescene = time.time()
            if time.time() - self.removescene > 3:
                self.dismiss_modal_scene()
            self.death = (SpriteNode(position = (self.screen_center_x, self.screen_center_y),
                                     parent = self,
                                     scale = 1,
                                     size = (self.size_of_screen_x * self.size_of_screen_x, self.size_of_screen_y * self.size_of_screen_x),
                                     alpha = 0.5))
            self.dead = LabelNode(text = 'you died!',
                                       position = (self.screen_center_x, self.screen_center_y),
                                       parent = self,
                                       scale = 1.25,
                                       color = '#a50000',
                                       font = ('CopperPlate-Light', 60))
            for monster in self.monsters:
                monster.remove_from_parent()
                self.monsters.remove(monster)
            for monster in self.monsters:
                monster.remove_from_parent()
                self.monsters.remove(monster)
                
        if time.time() - self.regentime >= 5 and globals.fullhealth - self.health >= globals.overtimeregen and self.health != 0:
            self.regentime = time.time()
            self.health = self.health + globals.overtimeregen
            self.regenover5.append(LabelNode(text = '+' + str(globals.overtimeregen),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 250 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#54ff2f',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 25),
                                      parent = self))
        
        if self.currentroundkills == self.roundkills:
            self.state = 'run'
            self.currentround = self.currentround + 1
            self.currentroundkills = 0
            self.roundkills = self.currentround * 3
            self.monsterspawned = 0
            self.timerroundup = 0
            self.roundup.append(LabelNode(text = 'ROUND ' + str(self.currentround),
                                      position = (self.screen_center_x, self.screen_center_y + 100),
                                      color = 'black',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 50),
                                      parent = self))
            for roundups in self.roundup:
                roundups.run_action(Action.fade_to(0, 5))
                roundups.run_action(Action.move_to(roundups.position.x, self.screen_center_y - 50, 5))
                if roundups.position.y <= self.screen_center_x - 40:
                    self.state = 'stand'
                    roundups.remove_from_parent()
                    self.roundup.remove(roundups)
                
        #MonsterSpawn
        self.creationrate = random.randint(1, 120)
        if self.monsterspawned < self.roundkills and self.creationrate <= self.monster_attack_rate:
            self.monsterspawned = self.monsterspawned + 1
            self.add_monster()
        
        for dmglabel in self.dmglabels:
            self.timerdmglabel = time.time()
            dmglabel.run_action(Action.fade_to(0,2))
            dmglabel.run_action(Action.move_to(dmglabel.position.x, 250, 2))
            if dmglabel.position.y <= 260:
                dmglabel.remove_from_parent()
                self.dmglabels.remove(dmglabel)
        
        for armormove in self.blocklabels:
            self.timerblock = 0
            armormove.run_action(Action.fade_to(0,3))
            armormove.run_action(Action.move_to(armormove.position.x, 150, 3))
            if armormove.position.y <= 160:
                armormove.remove_from_parent()
                self.blocklabels.remove(armormove)
        
        for regenovertime in self.regenover5:
            self.timerregen = 0
            regenovertime.run_action(Action.fade_to(0,3))
            regenovertime.run_action(Action.move_to(regenovertime.position.x, 150, 3))
            if regenovertime.position.y <= 160:
                regenovertime.remove_from_parent()
                self.regenover5.remove(regenovertime)
                
        #CharaterActions
        if self.state == 'attack':
            
            self.charater.position = (self.screen_center_x, 210)
            if self.rotationc <= self.swingspeed:
                self.charater.texture = Texture('./assets/sprites/game/swing1.PNG')
            elif self.rotationc > self.swingspeed and self.rotationc <= (self.swingspeed * 2):
                self.charater.texture = Texture('./assets/sprites/game/swing2.PNG')
            elif self.rotationc > (self.swingspeed * 2) and self.rotationc <= (self.swingspeed * 3):
                self.charater.texture = Texture('./assets/sprites/game/swing3.PNG')
            elif self.rotationc > (self.swingspeed * 3) and self.rotationc <= (self.swingspeed * 4):
                self.charater.texture = Texture('./assets/sprites/game/swing4.PNG')
            elif self.rotationc > (self.swingspeed * 4) and self.rotationc <= (self.swingspeed * 5):
                self.charater.texture = Texture('./assets/sprites/game/swing5.PNG')
            elif self.rotationc > (self.swingspeed * 5) and self.rotationc <= (self.swingspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/swing6.PNG')
            elif self.rotationc > (self.swingspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/swing6.PNG')
                self.rotationc = 1
                self.state = 'run'
                
            self.waitattack = self.fullatk + time.time()
        elif self.state == 'run':
            self.charater.position = (self.screen_center_x, 200)
            if self.rotationc <= self.runspeed:
                self.charater.texture = Texture('./assets/sprites/game/step1.PNG')
            elif self.rotationc > self.runspeed and self.rotationc <= (self.runspeed * 2):
                self.charater.texture = Texture('./assets/sprites/game/step2.PNG')
            elif self.rotationc > (self.runspeed * 2) and self.rotationc <= (self.runspeed * 3):
                self.charater.texture = Texture('./assets/sprites/game/step3.PNG')
            elif self.rotationc > (self.runspeed * 3) and self.rotationc <= (self.runspeed * 4):
                self.charater.texture = Texture('./assets/sprites/game/step4.PNG')
            elif self.rotationc > (self.runspeed * 4) and self.rotationc <= (self.runspeed * 5):
                self.charater.texture = Texture('./assets/sprites/game/step5.PNG')
            elif self.rotationc > (self.runspeed * 5) and self.rotationc <= (self.runspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/step6.PNG')
            elif self.rotationc > (self.runspeed * 6) and self.rotationc <= (self.runspeed * 7):
                self.charater.texture = Texture('./assets/sprites/game/step7.PNG')
            elif self.rotationc > (self.runspeed * 7) and self.rotationc <= (self.runspeed * 8):
                self.charater.texture = Texture('./assets/sprites/game/step8.PNG')
            elif self.rotationc > (self.runspeed * 8):
                self.charater.texture = Texture('./assets/sprites/game/step8.PNG')
                self.rotationc = 0
                
        elif self.state == 'stand':
            self.charater.position = (self.screen_center_x, 200)
            self.charater.texture = Texture('./assets/sprites/game/defaultguy.PNG')
        
        elif self.state == 'dead':
            self.charater.position = (self.screen_center_x, 200)
            self.charater.texture = Texture('assets/sprites/game/dead.PNG')

        
        for monster in self.monsters:
            if monster.position.y == 280:
                if self.monsterattack <= 50:
                     monster.position.y = 280
                     monster.texture = Texture('assets/sprites/game/straightreaper.PNG')
                elif self.monsterattack > 50 and self.monsterattack <= 55:
                    self.armorchancerole = random.randint(self.armor, 100)
                    monster.position.y = 270
                    monster.texture = Texture('assets/sprites/game/leftreaper.PNG')
                    if self.currentarmor <= 0:
                        self.currentarmor = 0
                        self.armor = 0
                        self.armorchancerole = 1000
                    if not self.armorchancerole <= self.armor:
                        self.health = self.health - random.randint(0,1 + round(self.currentround / 2))
                    else:
                        self.currentarmor = self.currentarmor - 1
                        self.blocklabels.append(LabelNode(text = 'BLOCK',
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 250 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#d3cccc',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 15),
                                      parent = self))
                elif self.monsterattack > 55 and self.monsterattack <= 105:
                    monster.position.y = 280
                    monster.texture = Texture('assets/sprites/game/straightreaper.PNG')
                elif self.monsterattack > 105 and self.monsterattack <= 110:
                    self.armorchancerole = random.randint(self.armor, 100)
                    monster.position.y = 270
                    monster.texture = Texture('assets/sprites/game/rightreaper.PNG')
                    if self.currentarmor <= 0:
                        self.currentarmor = 0
                        self.armor = 0
                        self.armorchancerole = 1000
                    if not self.armorchancerole <= self.armor:
                        self.health = self.health - random.randint(0,1 + round(self.currentround / 2))
                    else:
                        self.currentarmor = self.currentarmor - 1
                        self.blocklabels.append(LabelNode(text = 'BLOCK',
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 250 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#d3cccc',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 15),
                                      parent = self))
                else:
                    monster.position.y = 280
                    self.monsterattack = 0
                    monster.texture = Texture('assets/sprites/game/straightreaper.PNG')
            if monster.position.y <= 310 and self.state == 'attack' and self.rotationc == 6:
                self.currentkills = self.currentkills + 1
                self.currentroundkills = self.currentroundkills + 1
                self.currentcoins = self.currentcoins + random.randint((2 + self.currentround),(9 + self.currentround))
                self.critchanceroll = random.randint(self.crit, 100)
                if self.critchanceroll <= self.crit:
                    self.dmglabels.append(LabelNode(text = str(random.randint(globals.playerdmglowest + globals.playerdmglowest*(globals.playercritdmg/100), globals.playerdmghighest + globals.playerdmghighest*(globals.playercritdmg/100))),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 350 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#b00000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 30),
                                      parent = self))
                else:
                    self.dmglabels.append(LabelNode(text = str(random.randint(globals.playerdmglowest, globals.playerdmghighest)),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 350 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#ff0000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 25),
                                      parent = self))
                monster.remove_from_parent()
                self.monsters.remove(monster)
        
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
        
        monsterMoveAction = Action.move_to(monster_end_position.x, 
                                         monster_end_position.y, 
                                         self.monster_attack_speed,
                                         TIMING_SINODIAL)
        self.monsters[len(self.monsters)-1].run_action(monsterMoveAction)
