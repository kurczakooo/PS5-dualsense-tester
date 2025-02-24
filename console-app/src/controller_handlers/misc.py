import config

def stop():
    config.is_running = False

def on_ps_button_pressed():
    print('----Testing stopped with PS button----')
    stop()
    
config.controller.btn_ps.on_down(on_ps_button_pressed)    
    
    
def on_error(error):
    print(f'An Error occured: {error}')
    stop()
    
config.controller.on_error(on_error)
#--------------------------------------------------------------------

def on_mute():
    if config.controller.microphone.is_muted:
        config.controller.microphone.set_unmuted()
    else:
        config.controller.microphone.set_muted()
    print(config.controller.microphone._get_value())

config.controller.btn_mute.on_down(on_mute)

#--------------------------------------------------------------------
#work on this, battery and connection type
def connection_info():
    print(f'Controller connected with: {config.controller.connection_type}')

def battery_info():
    battery_info = config.controller.battery.value
    print(battery_info)
    
#--------------------------------------------------------------------
def on_gyroscope_change(gyroscope):
    print(f'\rgyroscope change: {gyroscope}', end='', flush=True)


def on_accelerometer_change(accelerometer):
    print(f'\raccelerometer change: {accelerometer}', end='', flush=True)


def on_orientation_change(orientation):
    print(f'\rorientation change: {orientation}', end='', flush=True)


# config.controller.gyroscope.on_change(on_gyroscope_change)
# config.controller.accelerometer.on_change(on_accelerometer_change)
# config.controller.orientation.on_change(on_orientation_change)