from . import config 
from .controller_handlers import leds as leds 
from frontend import frontend_config
from .events import (l2_press_change_event, 
                     r2_press_change_event, 
                     left_analog_move_event, 
                     right_analog_move_event, 
                     finger_1_move_event, 
                     finger_2_move_event, 
                     gyro_sensor_continuous_event,
                     acc_sensor_continuous_event,
                     orient_sensor_continuous_event)

def on_l2_trigger():
    value = config.controller.left_trigger._get_value()
    config.l2_trigger_press = value
    frontend_config.frontend_app.app.event_generate(l2_press_change_event)
    
def on_r2_trigger():
    value = config.controller.right_trigger._get_value()
    config.r2_trigger_press = value
    frontend_config.frontend_app.app.event_generate(r2_press_change_event)

def bind_trigger_continuous_handlers():
    config.controller.left_trigger.on_change(on_l2_trigger)
    config.controller.right_trigger.on_change(on_r2_trigger)



def on_left_analog_move(value):
    config.left_analog_move = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(left_analog_move_event)

def on_right_analog_move(value):
    config.right_analog_move = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(right_analog_move_event)
    
def bind_analog_continuous_handlers():    
    config.controller.left_stick.on_change(on_left_analog_move)
    config.controller.right_stick.on_change(on_right_analog_move)



def on_touchpad__finger_1_move(value):
    config.touchpad_finger_1_active = value.active
    config.touchpad_finger_1_coords = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(finger_1_move_event)
    leds.set_lightbar_color(value.x, value.y)

def on_touchpad__finger_2_move(value):
    config.touchpad_finger_2_active = value.active
    config.touchpad_finger_2_coords = (value.x, value.y)
    frontend_config.frontend_app.app.event_generate(finger_2_move_event)

def bind_touchpad_continuous_handlers():
    config.controller.touch_finger_1.on_change(on_touchpad__finger_1_move)
    config.controller.touch_finger_2.on_change(on_touchpad__finger_2_move)
    
#--------------------------------------------------------------------
def on_gyroscope_change(gyroscope):
    config.gyroscope = gyroscope
    frontend_config.frontend_app.app.event_generate(gyro_sensor_continuous_event)


def on_accelerometer_change(accelerometer):
    config.accelerometer = accelerometer
    frontend_config.frontend_app.app.event_generate(acc_sensor_continuous_event)


def on_orientation_change(orientation):
    config.orientation = orientation
    frontend_config.frontend_app.app.event_generate(orient_sensor_continuous_event)

def bind_gyro_acc_orient_sensors():
    config.controller.gyroscope.on_change(on_gyroscope_change)
    config.controller.accelerometer.on_change(on_accelerometer_change)
    config.controller.orientation.on_change(on_orientation_change)