import main_menu_scene 
import game_scene 
import shop_scene 

class Globals():
    #stats
    global fullhealth
    fullhealth = 100
    global playerdmglowest
    playerdmglowest = 20
    global playerdmghighest
    playerdmghighest = 50
    global playercritchance
    playercritchance = 7.5
    global playercritdmglowest
    playercritdmglowest = playerdmglowest * 2
    global playercritdmghighest
    playercritdmghighest = playerdmghighest * 2
    global overtimeregen
    overtimeregen = 5
    global playerarmor
    playerarmor = 2.5
    global playeratkspeed
    playeratkspeed = 0.5
    
    #coins
    global coins
    coins = 0
    
    #monsters
    global damage_orc
    damage_orc = 20
    global health_orc
    health_orc = 50
    global speed_orc
    speed_orc = 35
    
    global damage_troll
    damage_troll = 15
    global health_troll
    health_troll = 100
    global speed_troll
    speed_troll = 35
    
    global damage_goblin
    damage_goblin = 10
    global health_goblin
    health_goblin = 35
    global speed_goblin
    speed_goblin = 15
