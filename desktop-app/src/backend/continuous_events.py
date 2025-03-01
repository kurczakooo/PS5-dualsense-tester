from . import config 
from frontend import frontend_config

r2_press_change_event = "<<r2_press_change>>"
l2_press_change_event = "<<l2_press_change>>"

def on_l2_trigger():
    value = config.controller.left_trigger._get_value()
    config.l2_trigger_press = value
    frontend_config.frontend_app.app.event_generate(l2_press_change_event)
    
def on_r2_trigger():
    value = config.controller.right_trigger._get_value()
    config.r2_trigger_press = value
    frontend_config.frontend_app.app.event_generate(r2_press_change_event)

config.controller.left_trigger.on_change(on_l2_trigger)
config.controller.right_trigger.on_change(on_r2_trigger)


left_analog_move_event = "<<left_analog_move>>"
right_analog_move_event = "<<right_analog_move>>"
def on_left_analog_move(value):
    config.left_analog_move = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(left_analog_move_event)

def on_right_analog_move(value):
    config.right_analog_move = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(right_analog_move_event)
    
config.controller.left_stick.on_change(on_left_analog_move)
config.controller.right_stick.on_change(on_right_analog_move)