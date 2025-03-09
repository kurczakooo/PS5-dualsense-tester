from dualsense_controller import DualSenseController

is_running = True
mute = False
mute_led = False

l2_trigger_press = 0.0
r2_trigger_press = 0.0

left_analog_move = (0.0, 0.0)
right_analog_move = (0.0, 0.0)

touchpad_finger_1_coords = (0.0, 0.0)
touchpad_finger_2_coords = (0.0, 0.0)

controller = DualSenseController(device_index_or_device_info=0, microphone_initially_muted=False, microphone_invert_led=False)