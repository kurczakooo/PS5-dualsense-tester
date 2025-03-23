import tkinter


controller = None

device_info = None

battery_info = None

is_running = False

mute = False
mute_led = False

l2_trigger_press = 0.0
r2_trigger_press = 0.0

left_analog_move = (0.0, 0.0)
right_analog_move = (0.0, 0.0)

touchpad_finger_1_active = False # for later use
touchpad_finger_1_coords = (0.0, 0.0)
touchpad_finger_2_active = False
touchpad_finger_2_coords = (0.0, 0.0)

left_haptic_feedback = False
right_haptic_feedback = False

left_adaptive_trigger = False
left_adaptive_trigger_strength = 0
right_adaptive_trigger = False
right_adaptive_trigger_strength = 0