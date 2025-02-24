import config
from . import haptic_feedback as hf

def on_cross_button_pressed():
    print('Cross pressed')

def on_cross_button_released():
    print('Cross released')

config.controller.btn_cross.on_down(on_cross_button_pressed)
config.controller.btn_cross.on_up(on_cross_button_released)    
    
def on_circle_button_pressed():
    print('Circle pressed')
    hf.right_motor_vibration(255)

def on_circle_button_released():
    print('Circle released')
    hf.right_motor_vibration_off()

config.controller.btn_circle.on_down(on_circle_button_pressed)
config.controller.btn_circle.on_up(on_circle_button_released)
    
def on_square_button_pressed():
    print('Square pressed')
    hf.left_motor_vibration(255)

def on_square_button_released():
    print('Square released')
    hf.left_motor_vibration_off()

config.controller.btn_square.on_down(on_square_button_pressed)
config.controller.btn_square.on_up(on_square_button_released)    
    
def on_triangle_button_pressed():
    print('Triangle pressed')
    
def on_triangle_button_released():
    print('Triangle released')

config.controller.btn_triangle.on_down(on_triangle_button_pressed)
config.controller.btn_triangle.on_up(on_triangle_button_released)

def on_options_button_pressed():
    print('Options pressed')

def on_options_button_released():
    print('Options released')

config.controller.btn_options.on_down(on_options_button_pressed)
config.controller.btn_options.on_up(on_options_button_released)