import time
import threading
from dualsense_controller import DualSenseController

from backend import config
from backend.init_controller import init_controller
from backend.events import controller_disconnected_event
from backend.controller_handlers.misc import *
from frontend import frontend_config as frontend

def controllers_thread_task():

    device_infos = DualSenseController.enumerate_devices()

    if not device_infos:
        print("No DualSense Controller available.")
        frontend.frontend_app.app.event_generate(controller_disconnected_event, when='tail')
    else:
        device_indexes = [idx for idx in range(len(device_infos))]

        for idx in device_indexes:
            init_controller(idx, device_infos[idx])

        try:
            while config.is_running:
                time.sleep(0.001)

        except KeyboardInterrupt:
            print("----Testing stopped with keyboard----")
        
        config.controller.deactivate()


controllers_thread = threading.Thread(target=controllers_thread_task)

controllers_thread.start()
    
frontend.frontend_app.run()