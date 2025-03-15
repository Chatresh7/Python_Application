import tkinter as tk

window = tk.Tk()
window.geometry("400x450")
window.title("Tic Tac Toe")
window.config(bg="#000000")

count = 0
buttons = []
status_label = tk.Label(window, text="Player X's Turn", font=("Arial", 14), bg="#000000", fg="white")
status_label.pack()

def check_winner():
    winning_combinations = [
        [buttons[0], buttons[1], buttons[2]],
        [buttons[3], buttons[4], buttons[5]],
        [buttons[6], buttons[7], buttons[8]],
        [buttons[0], buttons[3], buttons[6]],
        [buttons[1], buttons[4], buttons[7]],
        [buttons[2], buttons[5], buttons[8]],
        [buttons[0], buttons[4], buttons[8]],
        [buttons[2], buttons[4], buttons[6]],
    ]
    
    for combo in winning_combinations:
        if combo[0]['text'] == combo[1]['text'] == combo[2]['text'] != ' ':
            for btn in combo:
                btn.config(bg="lightgreen")
            status_label.config(text=f"Player {combo[0]['text']} Wins!")
            disable_buttons()
            return
    
    # Check for draw condition
    if all(btn['text'] != ' ' for btn in buttons):
        for btn in buttons:
            btn.config(bg="gray", state="disabled")  # Disable buttons after a draw
            status_label.config(text="IT'S A DRAW !!!", fg="red", font=("Arial", 14, "bold"))
        return  


def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def press_button(btn):
    global count
    if btn['text'] == ' ':
        btn['text'] = 'X' if count % 2 == 0 else 'O'
        btn.config(fg="blue" if btn['text'] == 'X' else "red")
        count += 1
        check_winner()

        if not all(btn['text'] != ' ' for btn in buttons):  
            status_label.config(text="Player X's Turn" if count % 2 == 0 else "Player O's Turn")

def restart_game():
    global count
    count = 0
    status_label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(text=' ', state="normal", bg="yellow")

grid_frame = tk.Frame(window)
grid_frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(grid_frame, text=' ', bg="yellow", height=4, width=8, font=("Arial", 14), 
                        command=lambda b=len(buttons): press_button(buttons[b]))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)

restart_btn = tk.Button(window, text="Restart", bg="green", fg="white", font=("Arial", 14), 
                        command=restart_game)
restart_btn.pack(pady=10)

window.mainloop()
