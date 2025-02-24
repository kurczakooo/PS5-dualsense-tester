import time
import threading
import uvicorn
import API.server as api
from dualsense_controller import DualSenseController
import config
from controller_handlers.right_side_buttons import *
from controller_handlers.left_side_buttons import *
from controller_handlers.triggers import *
from controller_handlers.touchpad import *
from controller_handlers.analogs import *
from controller_handlers.haptic_feedback import *
from controller_handlers.misc import *

device_infos = DualSenseController.enumerate_devices()

if len(device_infos) < 1:
    raise Exception('No DualSense Controller available.')

for i in device_infos:
    print(i)

def controller_loop():
    config.controller.activate()
    while config.is_running:
        time.sleep(0.001)
    config.controller.deactivate()

controlller_thread = threading.Thread(target=controller_loop, daemon=True)
controlller_thread.start()

if __name__ == "__main__":
    uvicorn.run(api.app, host='127.0.0.1', port=8000)