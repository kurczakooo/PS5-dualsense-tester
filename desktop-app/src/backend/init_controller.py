from .state_events import bind_mic_handlers
from .press_release_events import bind_press_release_handlers
from .continuous_events import bind_trigger_continuous_handlers, bind_analog_continuous_handlers, bind_touchpad_continuous_handlers
from .controller_handlers.misc import bind_ps_press, bind_error
from . import config

def init_controller():
    config.is_running = True
    bind_error()
    bind_ps_press()
    bind_mic_handlers()
    bind_press_release_handlers()
    bind_trigger_continuous_handlers()
    bind_analog_continuous_handlers()
    bind_touchpad_continuous_handlers()
    