from .. import config

#need to make a nice slider for these s_max = 255
def left_motor_vibration(strength: int):
    config.controller.left_rumble.set(strength)
    
def left_motor_vibration_off():
    config.controller.left_rumble.set(0)
    
def toggle_left_haptic_feedback(strength: int):
    if config.left_haptic_feedback:
        left_motor_vibration_off()
        config.left_haptic_feedback = False
    else:
        left_motor_vibration(strength)
        config.left_haptic_feedback = True
    
    
def right_motor_vibration(strength: int):
    config.controller.right_rumble.set(strength)
    
def right_motor_vibration_off():
    config.controller.right_rumble.set(0)
    
def toggle_right_haptic_feedback(strength: int):
    if config.right_haptic_feedback:
        right_motor_vibration_off()
        config.right_haptic_feedback = False
    else:
        right_motor_vibration(strength)
        config.right_haptic_feedback = True