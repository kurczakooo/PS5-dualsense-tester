from dualsense_controller import DualSenseController, InvalidDeviceIndexException

is_running = True
gyroscope = False

controller = DualSenseController(device_index_or_device_info=0, microphone_initially_muted=False, microphone_invert_led=False)


import asyncio