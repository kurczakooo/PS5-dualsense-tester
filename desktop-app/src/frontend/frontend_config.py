import customtkinter as ctk
from PIL import Image, ImageTk  
from backend import press_release_events as pre, state_events as se
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
            width=750, 
            height=540, 
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
            350, 380, anchor='nw', 
            text=self.microphone_text, 
            fill="white", 
            font=('Arial', 12, 'bold')
        )
        
        
        
        #set the event binds to switch images
        self.set_press_release_binds()
        #set state binds like muting mic or enabling adaptiva triggers
        self.set_controller_state_binds()

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

    def change_image(self, image_name: str):
        self.canvas.itemconfig(self.image_id, image=self.images.get(image_name))

    def set_press_release_binds(self):
        for button, (press, release) in pre.events.items():
            self.app.bind(press, lambda event, btn=button: self.change_image(btn))
            self.app.bind(release, lambda event: self.change_image("default"))
            
    def update_mute_text(self, event):
        mute, led =   config.mute, config.mute_led
        self.microphone_text = f"Muted: {mute}\n  LED: {led}"
        self.canvas.itemconfig(self.microphone_text_id, text=self.microphone_text)
            
    def set_controller_state_binds(self):
        self.app.bind(se.mute_event, self.update_mute_text)

    def run(self):
        self.app.mainloop()
        
        
frontend_app = App()