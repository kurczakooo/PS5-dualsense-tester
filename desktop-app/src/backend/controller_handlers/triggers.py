from .. import config

def on_left_trigger(value):
    print(f'\rleft trigger press: {value}  ', end="", flush=True)

def on_right_trigger(value):
    print(f'\rright trigger press: {value}  ', end="", flush=True)

config.controller.left_trigger.on_change(on_left_trigger)
config.controller.right_trigger.on_change(on_right_trigger)
