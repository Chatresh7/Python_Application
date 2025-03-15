from tkinter import *
from PIL import Image, ImageTk
import os

# Main window setup
main = Tk()
main.geometry("700x600+300+50")
main.title("Game Menu")

# Load and set background image
img = Image.open(r"C:\Users\DELL\CS_PROJECT\PROJ_MAIN\Interface_imgnew.jpg")
resized_image = img.resize((700, 600))
new_image = ImageTk.PhotoImage(resized_image)
bg_label = Label(main, image=new_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Button Styling
button_style = {
    "bg": "#F5F5DC",  # Deep Pink
    "fg": "black",  # Text color black
    "font": ("Arial", 14, "bold"),
    "width": 15,
    "height": 2,
    "bd": 5,  # Border thickness
    "relief": "ridge",  # Gives a 3D effect (ridge effect like outline)
    "highlightbackground": "white",  # White highlight (simulating outline)
    "highlightthickness": 3,  # Thickness of the white highlight
    "cursor": "hand2"
}

# Buttons
button1 = Button(main, text="Snake Game", **button_style, command=lambda: os.system(r"C:\Users\DELL\CS_PROJECT\PROJ_MAIN\Snakegame.py"))
button1.place(x=250, y=10)

button2 = Button(main, text="Tic Tac Toe", **button_style, command=lambda: os.system(r"C:\Users\DELL\CS_PROJECT\PROJ_MAIN\TicTacToe.py"))
button2.place(x=250, y=270)

button3 = Button(main, text="Age Calculator", **button_style, command=lambda: os.system(r"C:\Users\DELL\CS_PROJECT\PROJ_MAIN\AgeCalculator.py"))
button3.place(x=250, y=520)

# Run the main loop
main.mainloop()
