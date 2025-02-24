import config
from . import leds as leds 
from . import player_led as player_led

def on_touchpad_button_pressed():
    print('Touchpad pressed')
    player_led.brightness_high_player_leds()
    player_led.turn_on_all_player_leds()
     
def on_touchpad_button_released():
    print('Touchpad released')
    player_led.turn_off_all_player_leds()
     
config.controller.btn_touchpad.on_down(on_touchpad_button_pressed)
config.controller.btn_touchpad.on_up(on_touchpad_button_released)


def on_touchpad__finger_1_move(value):
    print(f'\rfinger 1 touch coords: {value}  ', end="", flush=True)
    leds.set_lightbar_color(value.x, value.y)

def on_touchpad__finger_2_move(value):
    print(f'\rfinger 2 touch coords: {value}  ', end="", flush=True)

config.controller.touch_finger_1.on_change(on_touchpad__finger_1_move)
config.controller.touch_finger_2.on_change(on_touchpad__finger_2_move)