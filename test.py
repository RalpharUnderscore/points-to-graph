import webbrowser

import tkinter as tk
from PIL import ImageTk, Image

import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title("Simple Graph Generator")
root.geometry("380x400")
root.resizable(False, False)

try:
    PROGRAM_ICON = ImageTk.PhotoImage(Image.open("placeholder.jpg"))
    root.iconphoto(True, PROGRAM_ICON)
except FileNotFoundError: # So stubborn
    pass


# Create Frames
frame_generator = tk.LabelFrame(root, text="Graph Generator")

# Graph Generator, Create Entries
gen_entry_x1 = tk.Entry(frame_generator, width=7)
gen_entry_y1 = tk.Entry(frame_generator, width=7)

gen_entry_x2 = tk.Entry(frame_generator, width=7)
gen_entry_y2 = tk.Entry(frame_generator, width=7)

# Graph Generator, Create and Grid Radiobuttons
GRAPHTYPE = ["Linear", "Exponential"]
selected_graphtype = tk.StringVar()
selected_graphtype.set("Linear")

for x in GRAPHTYPE:
    gen_graphtype = tk.Radiobutton(frame_generator, text=x, variable=selected_graphtype, value=x).grid(row=GRAPHTYPE.index(x)+3,column=0, columnspan=2, sticky="w")

# Graph Generator, Create Generate Graph Button
gen_generate_button = tk.Button(frame_generator, text="Generate \nGraph", bg="#7abfff", activebackground="#7abfff", height=2, width=13)

# Grid Links
tk.Label(root, text=" ").grid(row=0, column=0, pady=5)
tk.Button(root, text="Github", bg="#343634", fg="#ffffff", activebackground="#343634", activeforeground="#ffffff", command=lambda: webbrowser.open("https://github.com/RalpharUnderscore/simple-graph-gen")).grid(row=0, column=1, sticky="sw")
tk.Button(root, text="Linear Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/kwi1uxjyev")).grid(row=0, column=2, sticky="sw")
tk.Button(root, text="Expo Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/ggrnu5cx7x")).grid(row=0, column=3, sticky="sw")

# Grid Frames
frame_generator.grid(row=1, column=0, columnspan=99, padx=10, pady=5)

# Graph Generator, Grid Label
tk.Label(frame_generator, text="Point 1:", anchor="w").grid(row=0, column=0, padx=8, pady=5)
tk.Label(frame_generator, text="x", anchor="w").grid(row=0, column=1, padx=18)
tk.Label(frame_generator, text="y", anchor="w").grid(row=0, column=2, padx=18)

tk.Label(frame_generator, text=" ").grid(row=0, column=3, padx=10)

tk.Label(frame_generator, text="Point 2:", anchor="w").grid(row=0, column=4, padx=8)
tk.Label(frame_generator, text="x", anchor="w").grid(row=0, column=5, padx=18)
tk.Label(frame_generator, text="y", anchor="w").grid(row=0, column=6, padx=18)

tk.Label(frame_generator, text=" ").grid(row=0, column=7, padx=2)

tk.Label(frame_generator, text=" ").grid(row=2, column=0)

# Graph Generator, Grid Entries
gen_entry_x1.grid(row=1, column=1, pady=2)
gen_entry_y1.grid(row=1, column=2, pady=2)
gen_entry_x2.grid(row=1, column=5, pady=2)
gen_entry_y2.grid(row=1, column=6, pady=2)

# Graph Generator, Grid Generate Button
gen_generate_button.grid(row=3, column=5, columnspan=3, rowspan=2, sticky="w")


'''
x = np.linspace(0.9919, 2.5)
plt.plot(x, x**2)
plt.show()
'''

root.mainloop()
