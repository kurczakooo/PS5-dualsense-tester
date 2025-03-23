
pr_events = {
    "cross": ["<<x_pressed>>", "<<x_released>>"],
    "triangle": ["<<triangle_pressed>>", "<<triangle_released>>"],
    "square": ["<<square_pressed>>", "<<square_released>>"],
    "circle": ["<<circle_pressed>>", "<<circle_released>>"],
    "up": ["<<dpad_up_pressed>>", "<<dpad_up_released>>"],
    "down": ["<<dpad_down_pressed>>", "<<dpad_down_released>>"],
    "left": ["<<dpad_left_pressed>>", "<<dpad_left_released>>"],
    "right": ["<<dpad_right_pressed>>", "<<dpad_right_released>>"],
    "l1": ["<<l1_pressed>>", "<<l1_released>>"],
    "l2": ["<<l2_pressed>>", "<<l2_released>>"],
    "r1": ["<<r1_pressed>>", "<<r1_released>>"],
    "r2": ["<<r2_pressed>>", "<<r2_released>>"],
    "l3": ["<<l3_pressed>>", "<<l3_released>>"],
    "r3": ["<<r3_pressed>>", "<<r3_released>>"],
    "create": ["<<create_pressed>>", "<<create_released>>"],
    "options": ["<<options_pressed>>", "<<options_released>>"],
    "ps": ["<<ps_pressed>>", "<<ps_released>>"],
    "touchpad": ["<<touchpad_pressed>>", "<<touchpad_released>>"],
    "mute": ["<<microphone_pressed>>", "<<microphone_released>>"],
}

mute_event = "<<microphone_toggled>>"

r2_press_change_event = "<<r2_press_change>>"
l2_press_change_event = "<<l2_press_change>>"

left_analog_move_event = "<<left_analog_move>>"
right_analog_move_event = "<<right_analog_move>>"

finger_1_move_event = "<<finger_1_move>>"
finger_2_move_event = "<<finger_2_move>>"

device_info_available_event = "<<device_info>>"

battery_state_change_event = "<<battery_state_change>>"

gyro_sensor_continuous_event = "<<gryo_change_event>>"
acc_sensor_continuous_event = "<<acc_change_event>>"
orient_sensor_continuous_event = "<<orient_change_event>>"
