from tkinter import *
from tkinter import ttk
import random

## Initialize GUI
root = Tk()
root.title("Sudoku!")

################
   # Functions
################

def difficulty_menu():
    # Remove all widgets (starter question + buttons)
    for widget in root.winfo_children():
        widget.destroy()

    # Set a window size that fits everything comfortably
    root.geometry("900x700")

    difficulty_question = Label(
        root,
        text='How hard do you want it?!',
        anchor=CENTER,
        height=2,
        width=30,
        font=("Comic Sans MS", 36, "bold"),
        fg="red",
        wraplength=600
    )
    difficulty_question.pack(pady=(40, 30))

    baby_button = Button(
        root,
        text='Baby Mode',
        font=("Comic Sans MS", 24, "bold"),
        fg="white",
        bg="skyblue",
        activebackground="darkred",
        activeforeground="white",
        relief=RAISED,
        bd=5,
        cursor="hand2",
        width=14,
        height=1,
        command=lambda: generate_board('Baby')
    )
    baby_button.pack(pady=10)

    boring_button = Button(
        root,
        text='Boring',
        font=("Comic Sans MS", 24, "bold"),
        fg="white",
        bg="grey",
        activebackground="darkred",
        activeforeground="white",
        relief=RAISED,
        bd=5,
        cursor="hand2",
        width=14,
        height=1,
        command=lambda: generate_board('Normal')
    )
    boring_button.pack(pady=10)

    hard_button = Button(
        root,
        text='I can take it',
        font=("Comic Sans MS", 24, "bold"),
        fg="white",
        bg="red",
        activebackground="darkred",
        activeforeground="white",
        relief=RAISED,
        bd=5,
        cursor="hand2",
        width=14,
        height=1,
        command=lambda: generate_board('Hard')
    )
    hard_button.pack(pady=10)

    extreme_button = Button(
        root,
        text='EXXXTREME!!!',
        font=("Comic Sans MS", 24, "bold"),
        fg="white",
        bg="darkred",
        activebackground="black",
        activeforeground="white",
        relief=RAISED,
        bd=5,
        cursor="hand2",
        width=14,
        height=1,
        command=lambda: generate_board('Extreme')
    )
    extreme_button.pack(pady=10)

def generate_puzzle(user_level: str):
    # Create Empty Board
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(board, row, col, num):
        if num in board[row]:
            return False
        if num in [board[r][col] for r in range(9)]:
            return False
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False
        return True

    def fill_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    fill_board(sudoku_array)

    # Remove numbers based on difficulty
    removed_squares = {'Baby': 1, 'Normal': 40, 'Hard': 60, 'Extreme': 64}.get(user_level, 40)

    while removed_squares > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if sudoku_array[row][col] != 0:
            sudoku_array[row][col] = 0
            removed_squares -= 1

    return sudoku_array


def close_app():
    root.destroy()

def generate_board(user_level: str):
    # Remove all widgets
    for widget in root.winfo_children():
        widget.destroy()

    current_puzzle = generate_puzzle(user_level)
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
            value = current_puzzle[r][c]
            btn = Button(
                root,
                text= "" if value == 0 else str(value),
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

################
# Opening Screen
################
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
    command = difficulty_menu
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
