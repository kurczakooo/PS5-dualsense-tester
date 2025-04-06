from dualsense_controller import DualSenseController
from . import config
import time
import threading


def controllers_thread_task(device_infos, device_indexes):
        from .init_controller import init_controller
        for idx in device_indexes:
            init_controller(idx, device_infos[idx])

        try:
            while config.is_running:
                time.sleep(0.001)
            config.controller.deactivate()

        except KeyboardInterrupt:
            print("----Testing stopped with keyboard----")


def look_for_controllers():
    device_infos = DualSenseController.enumerate_devices()

    if not device_infos:
        print("No DualSense Controller available.")
        return False
    else:
        device_indexes = [idx for idx in range(len(device_infos))]
        print(device_indexes)
        controllers_thread = threading.Thread(target=controllers_thread_task, args=[device_infos, device_indexes])
        controllers_thread.start()
        return True