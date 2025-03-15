import datetime
import tkinter as tk
from tkinter import messagebox

# Main window setup
window = tk.Tk()
window.geometry("400x350+500+200")
window.title("Age Calculator")
window.config(bg="#222831")

# Styling
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
result_font = ("Arial", 14, "bold")

# Labels
tk.Label(window, text="Enter Your Details", font=("Arial", 16, "bold"), bg="#222831", fg="white").grid(column=0, row=0, columnspan=2, pady=10)
tk.Label(window, text="Name:", font=label_font, bg="#222831", fg="white").grid(column=0, row=1, pady=5, sticky="w")
tk.Label(window, text="Year:", font=label_font, bg="#222831", fg="white").grid(column=0, row=2, pady=5, sticky="w")
tk.Label(window, text="Month:", font=label_font, bg="#222831", fg="white").grid(column=0, row=3, pady=5, sticky="w")
tk.Label(window, text="Day:", font=label_font, bg="#222831", fg="white").grid(column=0, row=4, pady=5, sticky="w")

# Entry Fields
nameEntry = tk.Entry(window, font=entry_font, width=20)
nameEntry.grid(column=1, row=1, padx=10, pady=5)
yearEntry = tk.Entry(window, font=entry_font, width=20)
yearEntry.grid(column=1, row=2, padx=10, pady=5)
monthEntry = tk.Entry(window, font=entry_font, width=20)
monthEntry.grid(column=1, row=3, padx=10, pady=5)
dateEntry = tk.Entry(window, font=entry_font, width=20)
dateEntry.grid(column=1, row=4, padx=10, pady=5)

result_label = tk.Label(window, text="", font=result_font, bg="#222831", fg="yellow")
result_label.grid(column=0, row=6, columnspan=2, pady=10)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

def getInput():
    try:
        name = nameEntry.get().strip()
        year = int(yearEntry.get())
        month = int(monthEntry.get())
        day = int(dateEntry.get())

        birth_date = datetime.date(year, month, day)  
        person = Person(name, birth_date)

        result_label.config(text=f"Hey {person.name}! You are {person.age()} years old!", fg="lightgreen")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date!")

# Button
button = tk.Button(window, text="Calculate Age", font=button_font, bg="yellow", fg="black", command=getInput)
button.grid(column=0, row=5, columnspan=2, pady=10)

window.mainloop()
