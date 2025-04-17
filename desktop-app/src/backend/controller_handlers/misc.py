from .. import config
from . import adaptive_triggers as at
from . import haptic_feedback as hf
from . import player_led as pl
from frontend import frontend_config
from ..events import controller_disconnected_event

def reset_controller():
    at.turn_off_left_adaptive_trigger()
    at.turn_off_right_adaptive_trigger()
    hf.left_motor_vibration_off()
    hf.right_motor_vibration_off()
    pl.brightness_high_player_leds()
    pl.turn_off_all_player_leds()
    
def stop():
    reset_controller()
    config.is_running = False
    frontend_config.frontend_app.app.event_generate(controller_disconnected_event, when='tail')
    # config.controller.deactivate()

def on_ps_button_pressed():
    print("PS PRESSED")
    
def bind_ps_press():    
    config.controller.btn_ps.on_down(on_ps_button_pressed)    
    
    
def on_error(error):
    print(f'An Error occured: {error}')
    frontend_config.frontend_app.app.event_generate(controller_disconnected_event, when='tail')
    stop()

    
def bind_error():    
    config.controller.on_error(on_error)