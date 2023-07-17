import webbrowser

import _exp as exp
import _lin as lin
import _plot as plotpy

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Graph Generator")
root.geometry("380x370")
root.resizable(False, False)


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


def CalculateButton():
    inputtype = selected_inputtype.get()
    if inputtype == "Points": ReadPointValues()
    else: ReadConstantValues()


# Retrieve the point values the user input
def ReadPointValues():
    try:
        x1 = float(twop_entry_x1.get())
        y1 = float(twop_entry_y1.get())
        x2 = float(twop_entry_x2.get())
        y2 = float(twop_entry_y2.get())
        
        domain_start = float(dom_entry_from.get())
        domain_end = float(dom_entry_to.get())

        domain = (domain_start, domain_end)
    except ValueError:
        messagebox.showerror(title="ValueError", message="ValueError: Missing or invalid values?")
        return

    point_one = (x1, y1)
    point_two = (x2, y2)

    mode = selected_graphtype_twop.get()

    if mode == "Linear": graph_parameters = lin.CreateLinearGraph(point_one, point_two)
    else: graph_parameters = exp.CreateExponentialGraph(point_one, point_two)
    
    if not isinstance(graph_parameters, float):
        if graph_parameters == "ZeroDivisionError": 
            messagebox.showerror(title="ZeroDivisionError", message="ZeroDivisionError: Perhaps the x-values of the two points are the same?")
            return
        if graph_parameters == "ValueError": 
            messagebox.showerror(title="ValueError", message="ValueError (domain error?): Make sure your y-values are > 0 when creating an exponential graph.")
            return
        
    GraphGeneration(graph_parameters, mode, domain)


def ReadConstantValues(): #// TODO: Calculate for Read Constant Values
    mode = selected_graphtype_cons.get()
    
    try:
        domain_start = float(dom_entry_from.get())
        domain_end = float(dom_entry_to.get())

        if mode == "Linear":
            valueone = float(cons_entry_m.get())
            valuetwo = float(cons_entry_c.get())
        else:
            valueone = float(cons_entry_a.get())
            valuetwo = float(cons_entry_b.get())
    except ValueError:
        messagebox.showerror(title="ValueError", message="ValueError: Missing or invalid values?")
        return
    
    domain = (domain_start, domain_end)
    
    GraphGeneration((valueone, valuetwo), mode, domain)



def GraphGeneration(graph_parameters, mode, domain):
    plotpy.CloseWindow()
    plotpy.plt.close()
    plotpy.GenerateGraph(graph_parameters, mode, domain)
    plotpy.OpenWindow()
    
    



# Create Frames
frame_twopoint = tk.LabelFrame(root)
frame_constants = tk.LabelFrame(root)
frame_domain = tk.LabelFrame(root, borderwidth=0)
frame_links = tk.LabelFrame(root, borderwidth=0)

# Create Input Type Radio Buttons
INPUTTYPE = ["Points", "Constants"]
selected_inputtype = tk.StringVar()
selected_inputtype.set("Points")

for x in INPUTTYPE:
    tk.Radiobutton(root, text=x, variable=selected_inputtype, value=x, command=ToggleInputTypes).grid(row=INPUTTYPE.index(x)*2+1,column=0, columnspan=1, sticky="w")

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
    

# root, Grid entry for domain settings
dom_entry_from = tk.Entry(frame_domain, width=7)
dom_entry_to = tk.Entry(frame_domain, width=7)



# Create Generate Graph Button
generate_button = tk.Button(frame_domain, text="Generate New Graph", height=2, bg="#7abfff", activebackground="#7abfff", command=CalculateButton)

# Grid Links
tk.Button(frame_links, text="Linear Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/kwi1uxjyev")).grid(row=1, column=0, padx=1, pady=5, sticky="e")
tk.Button(frame_links, text="Exponential Graph", bg="#60d15c", activebackground="#60d15c", command=lambda: webbrowser.open("https://www.desmos.com/calculator/ggrnu5cx7x")).grid(row=1, column=1, padx=1, pady=5, sticky="e")
tk.Button(frame_links, text="Github", bg="#343634", fg="#ffffff", activebackground="#343634", activeforeground="#ffffff", command=lambda: webbrowser.open("https://github.com/RalpharUnderscore/simple-graph-gen")).grid(row=1, column=2, padx=1, pady=5, sticky="e")


# Grid Frames
# NOTE TO SELF: Just put everything into frames, it's much easier to organize
frame_links.grid(row=1, column=8, sticky="e", padx=10)
frame_twopoint.grid(row=2, column=0, columnspan=10, padx=10, pady=5)
frame_constants.grid(row=4, column=0, columnspan=10, padx=10, pady=5)
frame_domain.grid(row=5, column=0, columnspan=10, padx=10, sticky="w")


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

# Frame Domain
tk.Label(frame_domain, text="Domain: from", anchor="w").grid(row=0, column=0, sticky="nsw", padx=4)
tk.Label(frame_domain, text=" to ", anchor="w").grid(row=0, column=2, sticky="nsw", padx=4)

dom_entry_from.grid(row=0, column=1, sticky="w", pady=2)
dom_entry_to.grid(row=0, column=3, sticky="w", pady=2,)

root.columnconfigure(5, weight=100) # Not sure what this actually does but it works lol
generate_button.grid(row=0, column=4, padx=25, sticky="nse")


# Constant Generators, Grid Entries
cons_entry_m.grid(row=1, column=2, pady=6)
cons_entry_c.grid(row=3, column=2, pady=6)
cons_entry_a.grid(row=1, column=5, pady=6)
cons_entry_b.grid(row=3, column=5, pady=6)






ToggleInputTypes() # Run function to disable unselected entries
root.mainloop() # The Hog Rider card is unlocked from the Spell Valley (Arena 5). He is a very fast building-targeting, melee troop with moderately high hitpoints and damage. He appears just like his Clash of Clans counterpart; a man with brown eyebrows, a beard, a mohawk, and a golden body piercing in his left ear who is riding a hog. A Hog Rider card costs 4 Elixir to deploy.
