from dualsense_controller import DualSenseController

is_running = True
mute = False
mute_led = False

controller = DualSenseController(device_index_or_device_info=0, microphone_initially_muted=False, microphone_invert_led=False)