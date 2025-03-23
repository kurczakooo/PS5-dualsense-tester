from . import config
from frontend import frontend_config
from .events import mute_event
from .events import battery_info_available_event

def on_mute_press():
    if config.controller.microphone.is_muted:
        config.controller.microphone.set_unmuted()
    else:
        config.controller.microphone.set_muted()
    
def on_mute_state_change():
    led = config.controller.microphone._get_value().led
    mute = config.controller.microphone._get_value().mute
    
    config.mute = mute
    config.mute_led = led
    
    frontend_config.frontend_app.app.event_generate(mute_event, when='tail')
   
def bind_mic_handlers():
    config.controller.microphone.on_change(on_mute_state_change)
    
    
def on_battery_state_change(state):
    config.battery_info = config.controller.battery.value
    print(config.battery_info)
    frontend_config.frontend_app.app.event_generate(battery_info_available_event, when='tail')
    
def bind_battery_handlers():
    config.controller.battery.on_charging(on_battery_state_change)
    config.controller.battery.on_discharging(on_battery_state_change)
    