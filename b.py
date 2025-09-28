import tkinter as tk
from tkinter import messagebox
import cmath as m

root = tk.Tk()
root.title("Quadratic Equation Solver")

label_a = tk.Label(root, text="a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

def solve():
    a = float(entry_a.get())
    
    # Calculate roots here and show result
    # (You can use your quadratic formula code)

    if a == 0:
        print("  a cannot be zero ")
        exit()
    else:
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = m.sqrt((b ** 2) - 4 * a * c)
        
        y = (-b + d) / (2 * a)
        x = (-b - d) / (2 * a)
    messagebox.showinfo("Result", f"Roots are {y} and {x}")

button = tk.Button(root, text="Solve", command=solve)
button.pack()

root.mainloop()