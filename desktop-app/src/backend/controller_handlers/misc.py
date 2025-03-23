from .. import config

def stop():
    config.is_running = False

def on_ps_button_pressed():
    print('----Testing stopped with PS button----')
    stop()
    
def bind_ps_press():    
    config.controller.btn_ps.on_down(on_ps_button_pressed)    
    
    
def on_error(error):
    print(f'An Error occured: {error}')
    stop()
    
def bind_error():    
    config.controller.on_error(on_error)
#--------------------------------------------------------------------

#work on this, connection type
def connection_info():
    print(f'Controller connected with: {config.controller.connection_type}')
    