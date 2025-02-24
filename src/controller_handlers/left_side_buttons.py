import config

def on_button_left_pressed():
    print('Left button pressed')

def on_button_left_released():
    print('Left button released')

config.controller.btn_left.on_down(on_button_left_pressed)
config.controller.btn_left.on_up(on_button_left_released)

def on_button_right_pressed():
    print('Right button pressed')

def on_button_right_released():
    print('Right button released')

config.controller.btn_right.on_down(on_button_right_pressed)
config.controller.btn_right.on_up(on_button_right_released)

def on_button_up_pressed():
    print('Up button pressed')

def on_button_up_released():
    print('Up button released')

config.controller.btn_up.on_down(on_button_up_pressed)
config.controller.btn_up.on_up(on_button_up_released)

def on_button_down_pressed():
    print('Down button pressed')

def on_button_down_released():
    print('Down button released')

config.controller.btn_down.on_down(on_button_down_pressed)
config.controller.btn_down.on_up(on_button_down_released)

def on_create_button_pressed():
    print('Create pressed')
    
def on_create_button_released():
    print('Create released')
    
config.controller.btn_create.on_down(on_create_button_pressed)
config.controller.btn_create.on_up(on_create_button_released)