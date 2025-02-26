import customtkinter as ctk
from PIL import Image, ImageTk

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
    "x": ImageTk.PhotoImage(Image.open("../assets/x_pressed.png").resize((750, 540))),
    "triangle": ImageTk.PhotoImage(Image.open("../assets/triangle_pressed.png").resize((750, 540))),
    "square": ImageTk.PhotoImage(Image.open("../assets/square_pressed.png").resize((750, 540))),
    "circle": ImageTk.PhotoImage(Image.open("../assets/circle_pressed.png").resize((750, 540))),
    "dpad_up": ImageTk.PhotoImage(Image.open("../assets/up_pressed.png").resize((750, 540))),
    "dpad_down": ImageTk.PhotoImage(Image.open("../assets/down_pressed.png").resize((750, 540))),
    "dpad_left": ImageTk.PhotoImage(Image.open("../assets/left_pressed.png").resize((750, 540))),
    "dpad_right": ImageTk.PhotoImage(Image.open("../assets/right_pressed.png").resize((750, 540))),
    "l1": ImageTk.PhotoImage(Image.open("../assets/l1_pressed.png").resize((750, 540))),
    "l2": ImageTk.PhotoImage(Image.open("../assets/l2_pressed.png").resize((750, 540))),
    "r1": ImageTk.PhotoImage(Image.open("../assets/r1_pressed.png").resize((750, 540))),
    "r2": ImageTk.PhotoImage(Image.open("../assets/r2_pressed.png").resize((750, 540))),
    "l3": ImageTk.PhotoImage(Image.open("../assets/l3_pressed.png").resize((750, 540))),
    "r3": ImageTk.PhotoImage(Image.open("../assets/r3_pressed.png").resize((750, 540))),
    "share": ImageTk.PhotoImage(Image.open("../assets/create_pressed.png").resize((750, 540))),
    "options": ImageTk.PhotoImage(Image.open("../assets/options_pressed.png").resize((750, 540))),
    "ps": ImageTk.PhotoImage(Image.open("../assets/ps_pressed.png").resize((750, 540))),
    "touchpad": ImageTk.PhotoImage(Image.open("../assets/touchpad_pressed.png").resize((750, 540))),
    "microphone": ImageTk.PhotoImage(Image.open("../assets/muted.png").resize((750, 540))),
}

# Ustawienie domyślnego obrazka
image_id = canvas.create_image(0, 0, anchor="nw", image=images["default"])

def change_image(button_name):
    """Zmienia obraz kontrolera na wersję z podświetlonym przyciskiem."""
    canvas.itemconfig(image_id, image=images.get(button_name, images["default"]))

# Testowe przyciski do symulacji wciśnięcia przycisków
buttons_frame = ctk.CTkFrame(master=tab_view.tab("player 1"))
buttons_frame.grid(row=1, column=0, pady=10)

buttons = [
    ("X", "x"), ("Trójkąt", "triangle"), ("Kwadrat", "square"), ("Kółko", "circle"),
    ("D-Pad ↑", "dpad_up"), ("D-Pad ↓", "dpad_down"), ("D-Pad ←", "dpad_left"), ("D-Pad →", "dpad_right"),
    ("L1", "l1"), ("L2", "l2"), ("R1", "r1"), ("R2", "r2"), 
    ("L3", "l3"), ("R3", "r3"), ("Share", "share"), ("Options", "options"),
    ("PS", "ps"), ("Touchpad", "touchpad"), ("Mute", "microphone"), ("Reset", "default")
]

for text, key in buttons:
    btn = ctk.CTkButton(buttons_frame, text=text, command=lambda k=key: change_image(k))
    btn.pack(side="left", padx=5)

