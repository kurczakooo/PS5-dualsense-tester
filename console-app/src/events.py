import config
import frontend_config
from functools import partial

events = {
    "cross": ["<<x_pressed>>", "<<x_released>>"],
    "triangle": ["<<triangle_pressed>>", "<<triangle_released>>"],
    "square": ["<<square_pressed>>", "<<square_released>>"],
    "circle": ["<<circle_pressed>>", "<<circle_released>>"],
    "up": ["<<dpad_up_pressed>>", "<<dpad_up_released>>"],
    "down": ["<<dpad_down_pressed>>", "<<dpad_down_released>>"],
    "left": ["<<dpad_left_pressed>>", "<<dpad_left_released>>"],
    "right": ["<<dpad_right_pressed>>", "<<dpad_right_released>>"],
    "l1": ["<<l1_pressed>>", "<<l1_released>>"],
    "l2": ["<<l2_pressed>>", "<<l2_released>>"],
    "r1": ["<<r1_pressed>>", "<<r1_released>>"],
    "r2": ["<<r2_pressed>>", "<<r2_released>>"],
    "l3": ["<<l3_pressed>>", "<<l3_released>>"],
    "r3": ["<<r3_pressed>>", "<<r3_released>>"],
    "create": ["<<create_pressed>>", "<<create_released>>"],
    "options": ["<<options_pressed>>", "<<options_released>>"],
    "ps": ["<<ps_pressed>>", "<<ps_released>>"],
    "touchpad": ["<<touchpad_pressed>>", "<<touchpad_released>>"],
    "mute": ["<<microphone_pressed>>", "<<microphone_released>>"],
}

def on_button_pressed(button_name, event_name):
    print(f'{button_name} pressed')
    frontend_config.app.event_generate(f'{event_name}', when="tail")

def on_button_released(button_name, event_name):
    print(f'{button_name} released')
    frontend_config.app.event_generate(f'{event_name}', when="tail")

for button, (press_event, release_event) in events.items():
    getattr(config.controller, f'btn_{button}').on_down(partial(on_button_pressed, button, press_event))
    getattr(config.controller, f'btn_{button}').on_up(partial(on_button_released, button, release_event))