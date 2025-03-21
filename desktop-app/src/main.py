import time
import threading
from dualsense_controller import DualSenseController

from backend import config
from backend.init_controller import init_controller
from backend.controller_handlers.misc import *
from frontend import frontend_config as frontend

def controllers_thread_task():
    device_infos = DualSenseController.enumerate_devices()

    if not device_infos:
        print("No DualSense Controller available.")
        return
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    for i in device_infos:
            labels = [
                "Path",
                "Vendor ID",
                "Product ID",
                "Serial Number",
                "Release Number",
                "Manufacturer",
                "Product",
                "Usage Page",
                "Usage",
                "Interface Number"
            ]

            values = [
                i.path,
                i.vendor_id,
                i.product_id,
                i.serial_number,
                i.release_number,
                i.manufacturer_string,
                i.product_string,
                i.usage_page,
                i.usage,
                i.interface_number
            ]

            for label, value in zip(labels, values):
                print(f"{label}: {value}")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    config.controller = DualSenseController(
                device_index_or_device_info=0,
                microphone_initially_muted=False,
                microphone_invert_led=False
            )
    
    init_controller()
    
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