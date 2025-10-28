from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sudoku!")

for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

for r in range(9):
    for c in range(9):
        frame = Frame(root, width=60, height=60)
        frame.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
        frame.grid_propagate(False)  # keep square shape

        btn = ttk.Button(frame, text="")
        btn.pack(expand=True, fill="both")

root.geometry("600x600")
root.mainloop()
