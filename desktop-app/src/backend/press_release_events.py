from . import config
from . import state_events
from frontend import frontend_config
from functools import partial
from .events import pr_events

def on_button_pressed(button_name, event_name):
    print(f'{button_name} pressed')
    
    if button_name == "mute":
        state_events.on_mute_press()
    
    frontend_config.frontend_app.app.event_generate(f'{event_name}', when="tail")

def on_button_released(button_name, event_name):
    print(f'{button_name} released')
    frontend_config.frontend_app.app.event_generate(f'{event_name}', when="tail")

def bind_press_release_handlers():
    for button, (press_event, release_event) in pr_events.items():
        getattr(config.controller, f'btn_{button}').on_down(partial(on_button_pressed, button, press_event))
        getattr(config.controller, f'btn_{button}').on_up(partial(on_button_released, button, release_event))