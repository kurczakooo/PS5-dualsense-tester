from dualsense_controller import DualSenseController
from dualsense_controller.core.hidapi import DeviceInfo

from .state_events import bind_mic_handlers, bind_battery_handlers
from .press_release_events import bind_press_release_handlers
from .continuous_events import (bind_trigger_continuous_handlers, 
                                bind_analog_continuous_handlers, 
                                bind_touchpad_continuous_handlers, 
                                bind_gyro_acc_orient_sensors)
from .controller_handlers.misc import bind_ps_press, bind_error

from . import config

from .events import device_info_available_event, battery_state_change_event, connection_type_available_event
from frontend import frontend_config



def init_controller(device_info_index: int, device_info: DeviceInfo):
    
    config.controller = DualSenseController(
            device_index_or_device_info=device_info_index,
            microphone_initially_muted=False,
            microphone_invert_led=False
    )
    
    config.is_running = True
    
    config.device_info = {"Vendor ID" : device_info.vendor_id,
                          "Product ID" : device_info.product_id,
                          "Serial Number" : device_info.serial_number,
                          "Release Number" : device_info.release_number,
                          "Manufacturer" : device_info.manufacturer_string,
                          "Product" : device_info.product_string}
    
    frontend_config.frontend_app.app.event_generate(device_info_available_event, when='tail')
    
    config.controller.activate()
    
    config.connection_info = config.controller.connection_type
    frontend_config.frontend_app.app.event_generate(connection_type_available_event, when='tail')
    
    config.battery_info = config.controller.battery.value
    frontend_config.frontend_app.app.event_generate(battery_state_change_event, when='tail')
    
    bind_error()
    bind_ps_press()
    bind_mic_handlers()
    bind_press_release_handlers()
    bind_trigger_continuous_handlers()
    bind_analog_continuous_handlers()
    bind_touchpad_continuous_handlers()
    bind_battery_handlers()
    bind_gyro_acc_orient_sensors()
