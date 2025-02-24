import config

def on_left_trigger(value):
    print(f'\rleft trigger press: {value}  ', end="", flush=True)

def on_right_trigger(value):
    print(f'\rright trigger press: {value}  ', end="", flush=True)

config.controller.left_trigger.on_change(on_left_trigger)
config.controller.right_trigger.on_change(on_right_trigger)

#implement functions to test haptic feedback and adaptive triggers

def on_r1_press():
    print('R1 pressed')
    
def on_r1_released():
    print('R1 released')
    
def on_l1_press():
    print('L1 pressed')
    
def on_l1_released():
    print('L1 released')
    
config.controller.btn_r1.on_down(on_r1_press)
config.controller.btn_r1.on_up(on_r1_released)
config.controller.btn_l1.on_down(on_l1_press)
config.controller.btn_l1.on_up(on_l1_press)