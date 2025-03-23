import customtkinter as ctk
from PIL import Image, ImageTk
from backend.controller_handlers.haptic_feedback import toggle_left_haptic_feedback, toggle_right_haptic_feedback
from backend.controller_handlers.adaptive_triggers import toggle_LAT, toggle_RAT
import backend.events as events
from backend import config

class App:
    
    def __init__(self):
        #create amd configure app
        self.app = ctk.CTk()
        self.app.title('PS5 CONTROLLER TESTER')
        self.app.geometry("1440x810")
        self.app.resizable(True, False)

        self.app.columnconfigure(0, weight=1)

        #create and configure tabs
        self.tab_view = ctk.CTkTabview(master=self.app)
        self.tab_view.pack(expand=True, fill="both", padx=20, pady=20)
        self.tab_view.add("player 1").columnconfigure(0, weight=1)
        self.tab_view.tab("player 1").rowconfigure(0, weight=1)
        self.tab_view.add("player 2")
        self.tab_view.add("player 3")
        self.tab_view.add("player 4")
        self.tab_view.set("player 1")

        #create and configure canvas on tab player 1
        self.canvas = ctk.CTkCanvas(
            master=self.tab_view.tab("player 1"), 
            width=1440,#750, 
            height=720,#540, 
            bg="#2B2B2B", #background color
            highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        
        #load controller images
        self.images = self.load_images()

        #load default image onto the canvas in tab player 1
        self.image_id = self.canvas.create_image(0, 0, anchor="nw", image=self.images.get('default'))
        
        #create text for microphone info
        self.microphone_text = "Muted: False\n  LED: False"
        self.microphone_text_id = self.canvas.create_text(
            335, 380, anchor='nw', 
            text=self.microphone_text, 
            fill="white", 
            font=('Arial', 12, 'bold'),
            justify="center"
        )
        
        #create text for device info
        self.device_info_text = "no device info available"
        self.device_info_text_id = self.canvas.create_text(
            20, 690, anchor="nw", 
            text=self.device_info_text, 
            fill="white", 
            font=('Arial', 11, 'bold'),
            justify="center"
        )
        
        #create text for battery info
        self.battery_info_text = "no battery info available"
        self.battery_text_id = self.canvas.create_text(
            335, 480, anchor="nw", 
            text="Battery State", 
            fill="green", 
            font=('Arial', 13, 'bold')
        )
        self.battery_info_text_id = self.canvas.create_text(
            325, 500, anchor="nw", 
            text=self.battery_info_text, 
            fill="white", 
            font=('Arial', 12, 'bold'),
            justify="center"
        )
        
        
        #create text for triggers press info
        self.r2_progress_text = "Press 0.0"
        self.l2_progress_text = "Press 0.0"
        self.r2_progress_text_id = self.canvas.create_text(
            440, 20, anchor='nw', 
            text=self.r2_progress_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        self.l2_progress_text_id = self.canvas.create_text(
            230, 20, anchor='nw', 
            text=self.l2_progress_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        
        #create text for triggers adaptive
        self.r2_adaptive_text = "Adaptive 0.0"
        self.l2_adaptive_text = "Adaptive 0.0"
        self.r2_adaptive_text_id = self.canvas.create_text(
            440, 40, anchor='nw', 
            text=self.r2_adaptive_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        self.l2_adaptive_text_id = self.canvas.create_text(
            230, 40, anchor='nw', 
            text=self.l2_adaptive_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )

        #create lines to resemble analog movement
        self.max_arrow_distance = 40
        self.left_analog_center = (280, 290)
        self.left_analog_arrow_end = self.left_analog_center
        self.left_analog_arrow_id = self.canvas.create_line(
            self.left_analog_center[0], self.left_analog_center[1],
            self.left_analog_arrow_end[0], self.left_analog_arrow_end[1],
            fill="red",
            smooth=True,
            width=5,
            arrow="last"
        )
        
        self.right_analog_center = (490, 290)
        self.right_analog_arrow_end = self.right_analog_center
        self.right_analog_arrow_id = self.canvas.create_line(
            self.right_analog_center[0], self.right_analog_center[1],
            self.right_analog_arrow_end[0], self.right_analog_arrow_end[1],
            fill="red",
            smooth=True,
            width=5,
            arrow="last"
        )
        
        #create text to show analogs movement
        self.left_analog_text = "(0.0, 0.0)"
        self.left_analog_text_id = self.canvas.create_text(
            230, 380, anchor='nw', 
            text=self.left_analog_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        
        self.right_analog_text = "(0.0, 0.0)"
        self.right_analog_text_id = self.canvas.create_text(
            460, 380, anchor='nw', 
            text=self.right_analog_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        
        #create dots to show fingers on touchpad
        self.x_factor = 1920/220
        self.y_factor = 1080/136
        self.finger_on_touchpad_start_cords = (275, 82)
        self.finger_1_coords = self.finger_on_touchpad_start_cords
        self.finger_1_circle_id = self.canvas.create_aa_circle(
            x_pos=self.finger_1_coords[0],
            y_pos=self.finger_1_coords[1],
            radius=3,
            fill=''
        )
        
        self.finger_2_coords = self.finger_on_touchpad_start_cords
        self.finger_2_circle_id = self.canvas.create_aa_circle(
            x_pos=self.finger_2_coords[0],
            y_pos=self.finger_2_coords[1],
            radius=3,
            fill=''
        )
        
        #set the event binds to switch images
        self.set_press_release_binds()
        #set state binds like muting mic or enabling adaptiva triggers
        self.set_controller_state_binds()
        #set continuous binds like trigger press or analogs
        self.set_continuous_binds()
        
        
        ########################################################################################################################
        #create buttons to toggle haptic feedback
        HF_strength = 255 # max, later think of a slider
        self.LHF_button = ctk.CTkButton(self.app, text="Left HF", command=lambda: toggle_left_haptic_feedback(HF_strength))
        self.RHF_button = ctk.CTkButton(self.app, text="Right HF", command=lambda: toggle_right_haptic_feedback(HF_strength))

        #create sliders to set adaptive triggers strength
        def lat_slider_handler(str):
            toggle_LAT(0, str)
            self.l2_adaptive_text = f"Adaptive {str}"
            self.canvas.itemconfig(self.l2_adaptive_text_id, text=self.l2_adaptive_text)
            
        def rat_slider_handler(str):
            toggle_RAT(0, str)
            self.r2_adaptive_text = f"Adaptive {str}"
            self.canvas.itemconfig(self.r2_adaptive_text_id, text=self.r2_adaptive_text)
        
        self.LAT_slider = ctk.CTkSlider(self.app, width=140, height=20, from_=0, to=255, command=lambda str: lat_slider_handler(round(str)))
        self.LAT_slider.set(0)
        self.RAT_slider = ctk.CTkSlider(self.app, width=140, height=20, from_=0, to=255, command=lambda str: rat_slider_handler(round(str)))
        self.RAT_slider.set(0)

        # positioning the buttons, sliders, etc
        # 20 pixels horizontal gap, 40 pixel vertical gap
        self.canvas.create_window(770, 50, window=self.LHF_button) 
        self.canvas.create_window(930, 50, window=self.RHF_button)
        self.canvas.create_window(770, 118, window=self.LAT_slider)
        self.canvas.create_window(930, 118, window=self.RAT_slider)
        ########################################################################################################################
        

    def load_images(self):
        images = {
            "default": ImageTk.PhotoImage(Image.open("../assets/white.png").resize((750, 540))),
            "cross": ImageTk.PhotoImage(Image.open("../assets/x_pressed.png").resize((750, 540))),
            "triangle": ImageTk.PhotoImage(Image.open("../assets/triangle_pressed.png").resize((750, 540))),
            "square": ImageTk.PhotoImage(Image.open("../assets/square_pressed.png").resize((750, 540))),
            "circle": ImageTk.PhotoImage(Image.open("../assets/circle_pressed.png").resize((750, 540))),
            "up": ImageTk.PhotoImage(Image.open("../assets/up_pressed.png").resize((750, 540))),
            "down": ImageTk.PhotoImage(Image.open("../assets/down_pressed.png").resize((750, 540))),
            "left": ImageTk.PhotoImage(Image.open("../assets/left_pressed.png").resize((750, 540))),
            "right": ImageTk.PhotoImage(Image.open("../assets/right_pressed.png").resize((750, 540))),
            "l1": ImageTk.PhotoImage(Image.open("../assets/l1_pressed.png").resize((750, 540))),
            "l2": ImageTk.PhotoImage(Image.open("../assets/l2_pressed.png").resize((750, 540))),
            "r1": ImageTk.PhotoImage(Image.open("../assets/r1_pressed.png").resize((750, 540))),
            "r2": ImageTk.PhotoImage(Image.open("../assets/r2_pressed.png").resize((750, 540))),
            "l3": ImageTk.PhotoImage(Image.open("../assets/l3_pressed.png").resize((750, 540))),
            "r3": ImageTk.PhotoImage(Image.open("../assets/r3_pressed.png").resize((750, 540))),
            "create": ImageTk.PhotoImage(Image.open("../assets/create_pressed.png").resize((750, 540))),
            "options": ImageTk.PhotoImage(Image.open("../assets/options_pressed.png").resize((750, 540))),
            "ps": ImageTk.PhotoImage(Image.open("../assets/ps_pressed.png").resize((750, 540))),
            "touchpad": ImageTk.PhotoImage(Image.open("../assets/touchpad_pressed.png").resize((750, 540))),
            "mute": ImageTk.PhotoImage(Image.open("../assets/mute_pressed.png").resize((750, 540))),
        }
        return images
# ------------------------------------------------------------------------
    def change_image(self, image_name: str):
        self.canvas.itemconfig(self.image_id, image=self.images.get(image_name))

    def set_press_release_binds(self):
        for button, (press, release) in events.pr_events.items():
            self.app.bind(press, lambda event, btn=button: self.change_image(btn))
            self.app.bind(release, lambda event: self.change_image("default"))
# ----------------------------------------------------------------------
    def update_mute_text(self, event):
        mute, led = config.mute, config.mute_led
        self.microphone_text = f"Muted: {mute}\nLED: {led}"
        self.canvas.itemconfig(self.microphone_text_id, text=self.microphone_text)
            
    def update_device_info_text(self, event):
        text = "        ".join(f"{key}: {value}" for key, value in config.device_info.items())
        self.device_info_text = text
        self.canvas.itemconfig(self.device_info_text_id, text=self.device_info_text)
            
    def update_battery_info_text(self, event):
        text = f"Level: {config.battery_info.level_percentage}\nFull: {config.battery_info.full}\nCharging: {config.battery_info.charging}"
        self.battery_info_text = text
        self.canvas.itemconfig(self.battery_info_text_id, text=self.battery_info_text)
            
    def set_controller_state_binds(self):
        self.app.bind(events.mute_event, self.update_mute_text)
        self.app.bind(events.device_info_available_event, self.update_device_info_text)
        self.app.bind(events.battery_info_available_event, self.update_battery_info_text)
        
# ----------------------------------------------------------------------
    def update_l2_progress_text(self, event):
        value = config.l2_trigger_press
        self.l2_progress_text = f"Press {str(value)}"
        self.canvas.itemconfig(self.l2_progress_text_id, text=self.l2_progress_text)
        
    def update_r2_progress_text(self, event):
        value = config.r2_trigger_press
        self.r2_progress_text = f"Press {str(value)}"
        self.canvas.itemconfig(self.r2_progress_text_id, text=self.r2_progress_text)
    
    def update_left_analog_position(self, event):
        pos = config.left_analog_move
        
        self.left_analog_text = str(pos)
        self.canvas.itemconfig(self.left_analog_text_id, text=self.left_analog_text)
        
        dx = pos[0] * self.max_arrow_distance
        dy = pos[1] * self.max_arrow_distance
        self.left_analog_arrow_end = (self.left_analog_center[0] + dx ,self.left_analog_center[1] - dy)
        self.canvas.coords(
            self.left_analog_arrow_id, 
            self.left_analog_center[0], self.left_analog_center[1],
            self.left_analog_arrow_end[0], self.left_analog_arrow_end[1])
    
    def update_right_analog_position(self, event):
        pos = config.right_analog_move
        
        self.right_analog_text = str(pos)
        self.canvas.itemconfig(self.right_analog_text_id, text=self.right_analog_text)
        
        dx = pos[0] * self.max_arrow_distance
        dy = pos[1] * self.max_arrow_distance
        self.right_analog_arrow_end = (self.right_analog_center[0] + dx ,self.right_analog_center[1] - dy)
        self.canvas.coords(
            self.right_analog_arrow_id, 
            self.right_analog_center[0], self.right_analog_center[1],
            self.right_analog_arrow_end[0], self.right_analog_arrow_end[1])
        
    def update_touchpad_finger_1_pos(self, event):
        touch_coordinates = config.touchpad_finger_1_coords
        active = config.touchpad_finger_1_active
        #divide by scale, cause the area is smaller, and add to starting points to offset accordingly
        x_scaled = touch_coordinates[0]/self.x_factor + self.finger_on_touchpad_start_cords[0]
        y_scaled = touch_coordinates[1]/self.y_factor + self.finger_on_touchpad_start_cords[1]

        self.finger_1_coords = (x_scaled, y_scaled)
        self.canvas.coords(
            self.finger_1_circle_id,
            self.finger_1_coords[0],
            self.finger_1_coords[1],
        )
        self.canvas.itemconfig(self.finger_1_circle_id, fill="red" if active else "")
         
    def update_touchpad_finger_2_pos(self, event):
        touch_coordinates = config.touchpad_finger_2_coords
        active = config.touchpad_finger_2_active
        #divide by scale, cause the area is smaller, and add to starting points to offset accordingly
        x_scaled = touch_coordinates[0]/self.x_factor + self.finger_on_touchpad_start_cords[0]
        y_scaled = touch_coordinates[1]/self.y_factor + self.finger_on_touchpad_start_cords[1]

        self.finger_2_coords = (x_scaled, y_scaled)
        self.canvas.coords(
            self.finger_2_circle_id,
            self.finger_2_coords[0],
            self.finger_2_coords[1],
        )
        self.canvas.itemconfig(self.finger_2_circle_id, fill="red" if active else "")
        
        
    def set_continuous_binds(self):
        self.app.bind(events.l2_press_change_event, self.update_l2_progress_text)
        self.app.bind(events.r2_press_change_event, self.update_r2_progress_text)
        
        self.app.bind(events.left_analog_move_event, self.update_left_analog_position)
        self.app.bind(events.right_analog_move_event, self.update_right_analog_position)
        
        self.app.bind(events.finger_1_move_event, self.update_touchpad_finger_1_pos)
        self.app.bind(events.finger_2_move_event, self.update_touchpad_finger_2_pos)
        
# ----------------------------------------------------------------------
    def run(self):
        self.app.mainloop()
        
        
frontend_app = App()