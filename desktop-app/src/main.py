import threading
from dualsense_controller import DualSenseController

from backend.look_for_controllers import controllers_thread_task
from backend.events import controller_disconnected_event
from backend.controller_handlers.misc import *
from frontend import frontend_config as frontend


device_infos = DualSenseController.enumerate_devices()

if not device_infos:
    print("No DualSense Controller available.")
    # frontend.frontend_app.app.after(500, 
                                    # lambda: frontend.frontend_app.app
                                    # .event_generate(controller_disconnected_event, when='tail'))
else:
    device_indexes = [idx for idx in range(len(device_infos))]
    controllers_thread = threading.Thread(target=controllers_thread_task, args=[device_infos, device_indexes])
    controllers_thread.start()
    
    
frontend.frontend_app.run()