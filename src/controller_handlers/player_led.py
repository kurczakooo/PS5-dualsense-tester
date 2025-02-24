import config
from time import sleep
import asyncio

def turn_on_all_player_leds():
    config.controller.player_leds.set_all()
    
def turn_off_all_player_leds():
    config.controller.player_leds.set_off()
#--------------------------------------------------------------------
def brightness_high_player_leds():
    config.controller.player_leds.set_brightness_high()

def brightness_medium_player_leds():
    config.controller.player_leds.set_brightness_medium()

def brightness_low_player_leds():
    config.controller.player_leds.set_brightness_low()
#--------------------------------------------------------------------
def turn_on_center_player_leds():
    config.controller.player_leds.set_center()
    
def turn_on_inner_player_leds():
    config.controller.player_leds.set_inner()
    
def turn_on_outer_player_leds():
    config.controller.player_leds.set_outer()
#--------------------------------------------------------------------

#this doesn't work, sleeps are no bueno, make it so you turn on the test mode,
#and either use buttons inapp, or controller buttons to control the leds
def test_player_leds():
    turn_on_all_player_leds()
    brightness_high_player_leds()
    sleep(1)
    brightness_medium_player_leds()
    sleep(1)
    brightness_low_player_leds()
    sleep(1)
    brightness_high_player_leds()
    sleep(1)
    turn_off_all_player_leds()
    sleep(1)
    turn_on_center_player_leds()
    sleep(1)
    turn_on_inner_player_leds()
    sleep(1)
    turn_on_outer_player_leds()
    sleep(1)
    turn_off_all_player_leds()
    print('player leds test success')