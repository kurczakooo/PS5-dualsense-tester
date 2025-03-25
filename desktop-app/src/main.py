import time
import threading
from dualsense_controller import DualSenseController

from backend import config
from backend.init_controller import init_controller
from backend.controller_handlers.misc import *
from frontend import frontend_config as frontend

def controllers_thread_task():
    while True:
            try:
                device_infos = DualSenseController.enumerate_devices()

                if not device_infos:
                    print("No DualSense Controller available. Waiting for connection...")
                    time.sleep(1)  # Czekaj na ponowne podłączenie
                    continue  # Spróbuj ponownie enumerować urządzenia
                
                device_indexes = [idx for idx in range(len(device_infos))]

                for idx in device_indexes:
                    init_controller(idx, device_infos[idx])
                
                while config.is_running:
                    time.sleep(0.001)

            except OSError as e:
                print(f"Controller disconnected: {e}. Waiting for reconnection...")
                time.sleep(1)  # Czekaj chwilę przed ponowną próbą

            except KeyboardInterrupt:
                print("----Testing stopped with keyboard----")
                break
            
    config.controller.deactivate()


controllers_thread = threading.Thread(target=controllers_thread_task)
controllers_thread.start()

frontend.frontend_app.run()