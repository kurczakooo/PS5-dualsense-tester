from .. import config

def on_left_analog_move(value):
    print(f'\rleft analog: {value}    ', end='', flush=True)

def on_right_analog_move(value):
    print(f'\rright analog: {value}    ', end='', flush=True)
    
config.controller.left_stick.on_change(on_left_analog_move)
config.controller.right_stick.on_change(on_right_analog_move)
