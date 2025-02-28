import customtkinter as ctk
from PIL import Image, ImageTk

import events

app = ctk.CTk()
app.title('PS5 CONTROLLER TESTER')
app.geometry("1440x810")
app.resizable(True, False)

app.columnconfigure(0, weight=1)

tab_view = ctk.CTkTabview(master=app)
tab_view.pack(expand=True, fill="both", padx=20, pady=20)
tab_view.add("player 1").columnconfigure(0, weight=1)
tab_view.tab("player 1").rowconfigure(0, weight=1)
tab_view.add("player 2")
tab_view.add("player 3")
tab_view.add("player 4")
tab_view.set("player 1")


canvas = ctk.CTkCanvas(
    master=tab_view.tab("player 1"), 
    width=750, 
    height=540, 
    bg="#2B2B2B", #background color
    highlightthickness=0)
canvas.grid(row=0, column=0)

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
    "mute": ImageTk.PhotoImage(Image.open("../assets/muted.png").resize((750, 540))),
}

# Ustawienie domyślnego obrazka
image_id = canvas.create_image(0, 0, anchor="nw", image=images.get('default'))

def change_image(image_name: str):
    canvas.itemconfig(image_id, image=images.get(image_name))

for button, (press, release) in events.events.items():
    app.bind(press, lambda event, btn=button: change_image(btn))
    app.bind(release, lambda event: change_image("default"))
