from tkinter import *
from tkinter import ttk
import random

## Functions

def generate_puzzle():
    # Remove all widgets (starter question + buttons)
    for widget in root.winfo_children():
        widget.destroy()

    # Create Empty Board
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]
    used_numbers = []

    # First row
    for index in range(9):
        while sudoku_array[0][index] == 0:
            placeholder_value = random.randint(1,9)
            if placeholder_value not in used_numbers:
                sudoku_array[0][index] = placeholder_value
                used_numbers.append(placeholder_value)
    

    print(sudoku_array)
def close_app():
    root.destroy()

def generate_board():
    # Remove all widgets (starter question + buttons)
    for widget in root.winfo_children():
        widget.destroy()

    # Configure the 9x9 grid
    for i in range(9):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    # Build 9x9 grid of cells
    for r in range(9):
        for c in range(9):
            # Outer frame acts as border
            border = Frame(root, bg="black", width=60, height=60)
            border.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
            border.grid_propagate(False)

            # Inner frame gives white background and padding
            cell = Frame(border, bg="white")
            cell.pack(expand=True, fill="both", padx=1, pady=1)

            # ttk Button inside the cell
            btn = ttk.Button(cell, text="")
            btn.pack(expand=True, fill="both")


## Initialize GUI
root = Tk()
root.title("Sudoku!")

starter_question = Label(
    root,
    text='Do you want to play Sudoku?!',
    anchor=CENTER,
    height=3,
    width=40,
    font=("Arial", 40, "bold"),
    fg="red",
    wraplength=400
)
starter_question.pack()

confirm_button = Button(
    root,
    text='YES!',
    font=("Arial", 28, "bold"),  # big and readable
    fg="white",                  # white text
    bg="red",                    # red background to match label’s text color
    activebackground="darkred",  # darker when pressed
    activeforeground="white",
    relief=RAISED,               # gives it a 3D border
    bd=5,                        # border thickness
    cursor="hand2",              # hand cursor on hover
    width=10,                    # adjusts button width
    height=2,                     # adjusts button height
    command = generate_puzzle
)
confirm_button.pack(pady=20)

loser_button = Button(
    root,
    text='NO!',
    font=("Arial", 28, "bold"),  # big and readable
    fg="white",                  # white text
    bg="blue",                    # red background to match label’s text color
    activebackground="darkblue",  # darker when pressed
    activeforeground="white",
    relief=RAISED,               # gives it a 3D border
    bd=5,                        # border thickness
    cursor="hand2",              # hand cursor on hover
    width=10,                    # adjusts button width
    height=2,                     # adjusts button height
    command = close_app
)
loser_button.pack(pady=20)

root.geometry("600x600")
root.mainloop()
