from tkinter import *
from tkinter import ttk
import random

## Initialize GUI
root = Tk()
root.title("Sudoku!")

## Functions
def generate_puzzle():
    # Remove all widgets (starter question + buttons)
    for widget in root.winfo_children():
        widget.destroy()

    # Create Empty Board
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]

    used_numbers = []
    for row_value in range(9):
        for column_value in range(9):
            while sudoku_array[row_value][column_value] == 0:
                placeholder_value = random.randint(1,9)
                if placeholder_value not in used_numbers:
                    sudoku_array[row_value][column_value] = placeholder_value
                    used_numbers.append(placeholder_value)
        used_numbers.clear()
    return sudoku_array

def close_app():
    root.destroy()

def generate_board():
    # Remove all widgets
    for widget in root.winfo_children():
        widget.destroy()

    current_puzzle = generate_puzzle()
    board_size = 540  # total pixel size of the board
    cell_size = board_size // 9  # 60 pixels per cell

    # Create a Canvas to draw thick grid lines
    canvas = Canvas(root, width=board_size, height=board_size, bg="white")
    canvas.pack(expand=True, fill="both")

    # Draw the grid lines
    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1  # thick lines every 3 cells
        # vertical line
        canvas.create_line(i*cell_size, 0, i*cell_size, board_size, width=line_width, fill="black")
        # horizontal line
        canvas.create_line(0, i*cell_size, board_size, i*cell_size, width=line_width, fill="black")

    # Place buttons on top of the canvas
    buttons = [[None for _ in range(9)] for _ in range(9)]
    for r in range(9):
        for c in range(9):
            btn = Button(
                root,
                text= current_puzzle[r][c],
                font=("Comic Sans MS", 20, "bold"),
                bg="white",
                relief=RIDGE
            )
            btn.place(
                x=c*cell_size + 1,   # +1 to not overlap thick line
                y=r*cell_size + 1,
                width=cell_size-2,    # -2 to fit inside grid lines
                height=cell_size-2
            )
            buttons[r][c] = btn

starter_question = Label(
    root,
    text='Do you want to play Sudoku?!',
    anchor=CENTER,
    height=3,
    width=40,
    font=("Comic Sans MS", 40, "bold"),  # <-- changed font
    fg="red",
    wraplength=400
)
starter_question.pack()

confirm_button = Button(
    root,
    text='YES!',
    font=("Comic Sans MS", 28, "bold"),  # <-- changed font
    fg="white",
    bg="red",
    activebackground="darkred",
    activeforeground="white",
    relief=RAISED,
    bd=5,
    cursor="hand2",
    width=10,
    height=2,
    command = generate_board
)
confirm_button.pack(pady=20)

loser_button = Button(
    root,
    text='NO!',
    font=("Comic Sans MS", 28, "bold"),  # <-- changed font
    fg="white",
    bg="blue",
    activebackground="darkblue",
    activeforeground="white",
    relief=RAISED,
    bd=5,
    cursor="hand2",
    width=10,
    height=2,
    command = close_app
)
loser_button.pack(pady=20)
root.mainloop()
