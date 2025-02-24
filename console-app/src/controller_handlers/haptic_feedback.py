import config

#need to make a nice slider for these
def left_motor_vibration(strength: int):
    config.controller.left_rumble.set(strength)
    
def left_motor_vibration_off():
    config.controller.left_rumble.set(0)
    
def right_motor_vibration(strength: int):
    config.controller.right_rumble.set(strength)
    
def right_motor_vibration_off():
    config.controller.right_rumble.set(0)