import webbrowser

import _exp as exp
import _lin as lin
import _plot as plotpy

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Graph Generator")
root.geometry("380x380")
root.resizable(True, True)

try:
    PROGRAM_ICON = ImageTk.PhotoImage(Image.open("placeholder.jpg"))
    root.iconphoto(True, PROGRAM_ICON)
except FileNotFoundError: # So stubborn
    pass

def ToggleInputTypes():
    inputtype = selected_inputtype.get()
    if inputtype == "Points":
        for child in frame_twopoint.winfo_children():
            child.configure(state="normal")

        for child in frame_constants.winfo_children():
            try: child.delete(0, tk.END)
            except AttributeError: pass
            child.configure(state="disabled")

    else:
        for child in frame_twopoint.winfo_children():
            child.configure(state="disabled")

        for child in frame_constants.winfo_children():
            try: child.delete(0, tk.END)
            except AttributeError: pass
            child.configure(state="normal")

        ConsToggleGraphType() # Above code enables all entries in constants frame, run this function to disable unselected ones

def ConsToggleGraphType():
    global cons_entry_m
    global cons_entry_c
    global cons_entry_a
    global cons_entry_b

    graphtype = selected_graphtype_cons.get()

    if graphtype == "Linear":
        cons_entry_m["state"] = "normal"
        cons_entry_c["state"] = "normal"

        cons_entry_a["state"] = "disabled"
        cons_entry_b["state"] = "disabled"
    else:
        cons_entry_a["state"] = "normal"
        cons_entry_b["state"] = "normal"

        cons_entry_m["state"] = "disabled"
        cons_entry_c["state"] = "disabled"

# Retrieve the point values the user input
def ReadPointValues():
    flagError = False
    try:
        x1 = float(twop_entry_x1.get())
        y1 = float(twop_entry_y1.get())
        x2 = float(twop_entry_x2.get())
        y2 = float(twop_entry_y2.get())
    except:
        flagError = True

    if flagError: return

    point_one = (x1, y1)
    point_two = (x2, y2)

    mode = selected_graphtype_twop.get()
    if mode == "Linear":
        graph_parameters = lin.CreateLinearGraph(point_one, point_two)
    else:
        graph_parameters = exp.CreateExponentialGraph(point_one, point_two)

    plotpy.plt.close()
    plotpy.GenerateGraph(graph_parameters, point_one, point_two, mode)


# Create Frames
frame_twopoint = tk.LabelFrame(root)
frame_constants = tk.LabelFrame(root)

# Create Input Type Radio Buttons
INPUTTYPE = ["Points", "Constants"]
selected_inputtype = tk.StringVar()
selected_inputtype.set("Points")

for x in INPUTTYPE:
    tk.Radiobutton(root, text=x, variable=selected_inputtype, value=x, command=ToggleInputTypes).grid(row=INPUTTYPE.index(x)*2+1,column=0, columnspan=99, sticky="w")

# Two Point Generators, Create Entries
twop_entry_x1 = tk.Entry(frame_twopoint, width=7)
twop_entry_y1 = tk.Entry(frame_twopoint, width=7)

twop_entry_x2 = tk.Entry(frame_twopoint, width=7)
twop_entry_y2 = tk.Entry(frame_twopoint, width=7)

# Constant Generators, Create Entries
cons_entry_m = tk.Entry(frame_constants, width=7)
cons_entry_c = tk.Entry(frame_constants, width=7)

cons_entry_a = tk.Entry(frame_constants, width=7)
cons_entry_b = tk.Entry(frame_constants, width=7)

# Create and Grid Radiobuttons that select graph type
GRAPHTYPE = ["Linear", "Exponential"]

selected_graphtype_twop = tk.StringVar()
selected_graphtype_twop.set("Linear")

selected_graphtype_cons = tk.StringVar()
selected_graphtype_cons.set("Linear")


for x in GRAPHTYPE:
    tk.Radiobutton(frame_twopoint, text=x, variable=selected_graphtype_twop, value=x).grid(row=GRAPHTYPE.index(x)+3,column=0, columnspan=2, sticky="w")
    tk.Radiobutton(frame_constants, text=f"{x}:", variable=selected_graphtype_cons, value=x, command=ConsToggleGraphType).grid(row=0,column=GRAPHTYPE.index(x)*4, sticky="w")
    

# Constant Generators, Create and Grid Radio Buttons


# Create Generate Graph Button
#generate_button = tk.Button(frame_twopoint, text="Generate \nNew Graph", bg="#7abfff", activebackground="#7abfff", height=2, width=13, command=ReadPointValues)

# Grid Links
tk.Label(root, text=" Graph Generator by Ralphar", font="TkDefaultFont 7 bold", anchor="sw").grid(row=0, column=0, pady=3)
tk.Button(root, text="Linear Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/kwi1uxjyev")).grid(row=0, column=1, sticky="se")
tk.Button(root, text="Exponential Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/ggrnu5cx7x")).grid(row=0, column=2, sticky="se")
tk.Button(root, text="Github", bg="#343634", fg="#ffffff", activebackground="#343634", activeforeground="#ffffff", command=lambda: webbrowser.open("https://github.com/RalpharUnderscore/simple-graph-gen")).grid(row=0, column=3, sticky="se")


# Grid Frames
frame_twopoint.grid(row=2, column=0, columnspan=99, padx=10, pady=5)
frame_constants.grid(row=4, column=0, columnspan=99, padx=10, pady=5)

# Two Point Generators, Grid Label
tk.Label(frame_twopoint, text="Point 1:", anchor="w").grid(row=0, column=0, padx=8, pady=5)
tk.Label(frame_twopoint, text="x", anchor="w").grid(row=0, column=1, padx=18)
tk.Label(frame_twopoint, text="y", anchor="w").grid(row=0, column=2, padx=18)

tk.Label(frame_twopoint, text=" ").grid(row=0, column=3, padx=10)

tk.Label(frame_twopoint, text="Point 2:", anchor="w").grid(row=0, column=4, padx=8)
tk.Label(frame_twopoint, text="x", anchor="w").grid(row=0, column=5, padx=18)
tk.Label(frame_twopoint, text="y", anchor="w").grid(row=0, column=6, padx=18)

tk.Label(frame_twopoint, text=" ").grid(row=0, column=7, padx=2)

tk.Label(frame_twopoint, text=" ").grid(row=2, column=0)

# Two Point Generators, Grid Entries
twop_entry_x1.grid(row=1, column=1, pady=2)
twop_entry_y1.grid(row=1, column=2, pady=2)
twop_entry_x2.grid(row=1, column=5, pady=2)
twop_entry_y2.grid(row=1, column=6, pady=2)

# Constant Generators, Grid Label
tk.Label(frame_constants, text="m:", anchor="w").grid(row=1, column=1, sticky="e")
tk.Label(frame_constants, text="c:", anchor="w").grid(row=3, column=1, sticky="e")
tk.Label(frame_constants, text="a:", anchor="w").grid(row=1, column=4, sticky="e")
tk.Label(frame_constants, text="b:", anchor="w").grid(row=3, column=4, sticky="e")

tk.Label(frame_constants, text=" ", anchor="w").grid(row=0, column=3, padx=30)
tk.Label(frame_constants, text=" ", anchor="w").grid(row=0, column=7, padx=7)
tk.Label(frame_constants, text=" ", anchor="w").grid(row=4, column=0)

# root, Grid Label
tk.Label(root, text="Domain: From", anchor="w").grid(row=5, column=0, sticky="w", padx=4)



# Constant Generators, Grid Entries
cons_entry_m.grid(row=1, column=2, pady=6)
cons_entry_c.grid(row=3, column=2, pady=6)
cons_entry_a.grid(row=1, column=5, pady=6)
cons_entry_b.grid(row=3, column=5, pady=6)



# Grid Generate Button
#generate_button.grid(row=3, column=5, columnspan=3, rowspan=2, sticky="w")






ToggleInputTypes() # Run function to disable unselected entries
root.mainloop() # The Hog Rider card is unlocked from the Spell Valley (Arena 5). He is a very fast building-targeting, melee troop with moderately high hitpoints and damage. He appears just like his Clash of Clans counterpart; a man with brown eyebrows, a beard, a mohawk, and a golden body piercing in his left ear who is riding a hog. A Hog Rider card costs 4 Elixir to deploy.
