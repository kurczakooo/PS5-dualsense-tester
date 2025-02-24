import config

def on_left_analog_move(value):
    print(f'\rleft analog: {value}    ', end='', flush=True)

def on_right_analog_move(value):
    print(f'\rright analog: {value}    ', end='', flush=True)
    
config.controller.left_stick.on_change(on_left_analog_move)
config.controller.right_stick.on_change(on_right_analog_move)

def on_l3_pressed():
    print('l3 pressed')

def on_l3_released():
    print('l3 released')

def on_r3_pressed():
    print('r3 pressed')
    
def on_r3_released():
    print('r3 released')
    
config.controller.btn_l3.on_down(on_l3_pressed)
config.controller.btn_l3.on_up(on_l3_released)
config.controller.btn_r3.on_down(on_r3_pressed)
config.controller.btn_r3.on_up(on_r3_released)