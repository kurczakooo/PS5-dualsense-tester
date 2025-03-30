from .. import config
from frontend import frontend_config
from ..events import controller_disconnected_event

def stop():
    config.controller.deactivate()
    config.is_running = False

def on_ps_button_pressed():
    # print('----Testing stopped with PS button----')
    print("PS PRESSED")
    stop()
    
def bind_ps_press():    
    config.controller.btn_ps.on_down(on_ps_button_pressed)    
    
    
def on_error(error):
    print(f'An Error occured: {error}')
    frontend_config.frontend_app.app.event_generate(controller_disconnected_event, when='tail')
    stop()

    
def bind_error():    
    config.controller.on_error(on_error)