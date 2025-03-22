from .. import config

#make also sliders for that -start pos [0,255] strength[0,255]
def set_left_adaptive_trigger(start_pos: int, strength: int):
    config.controller.left_trigger.effect.continuous_resistance(start_pos, strength)
    
def turn_off_left_adaptive_trigger():
    config.controller.left_trigger.effect.off()
    
def toggle_LAT(start_pos: int, strength: int):
    if strength == 0:
        turn_off_left_adaptive_trigger()
    else:
        set_left_adaptive_trigger(start_pos, strength)

def set_right_adaptive_trigger(start_pos: int, strength: int):
    config.controller.right_trigger.effect.continuous_resistance(start_pos, strength)
    
def turn_off_right_adaptive_trigger():
    config.controller.right_trigger.effect.off()