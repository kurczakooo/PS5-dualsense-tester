from .. import config

def turn_on_all_player_leds():
    config.controller.player_leds.set_all()
    
def turn_off_all_player_leds():
    config.controller.player_leds.set_off()
#--------------------------------------------------------------------
def set_brightness(val):
    if val == 1:
        config.controller.player_leds.set_brightness_low()
    elif val == 2:
        config.controller.player_leds.set_brightness_medium()
    elif val == 3:
        config.controller.player_leds.set_brightness_high()
#--------------------------------------------------------------------
def turn_on_center_player_leds():
    config.controller.player_leds.set_center()
    
def turn_on_inner_player_leds():
    config.controller.player_leds.set_inner()
    
def turn_on_outer_player_leds():
    config.controller.player_leds.set_outer()
#--------------------------------------------------------------------
