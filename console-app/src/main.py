import time
import threading
from dualsense_controller import DualSenseController

import config
from controller_handlers.triggers import *
from controller_handlers.touchpad import *
from controller_handlers.analogs import *
from controller_handlers.haptic_feedback import *
from controller_handlers.misc import *
import frontend_config as frontend

def controllers_thread_task():
    device_infos = DualSenseController.enumerate_devices()

    if len(device_infos) < 1:
        raise Exception('No DualSense Controller available.')

    for i in device_infos:
        print(i)

    config.controller.activate()

    try:
        while config.is_running:
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("----Testing stopped with keyboard----")
        
    config.controller.deactivate()


controllers_thread = threading.Thread(target=controllers_thread_task)
controllers_thread.start()

frontend.frontend_app.run()
