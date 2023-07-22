import webbrowser

import _exp as exp
import _lin as lin
import _plot as plotpy

import numpy as np
import warnings
import math

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# ! NOTE TO SELF: Please don't use Python and tkinter for multi-windowed programs again. It is so difficult to manage.

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
    global graph_parameters
    global mode
    global domain
    try:
        x1 = float(twop_entry_x1.get())
        y1 = float(twop_entry_y1.get())
        x2 = float(twop_entry_x2.get())
        y2 = float(twop_entry_y2.get())
        
        domain_start = float(dom_entry_from.get())
        domain_end = float(dom_entry_to.get())

        domain = (domain_start, domain_end)
    except ValueError:
        messagebox.showerror(title="ValueError", message="ValueError: Missing or invalid values.")
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
        if graph_parameters == "ZeroDivisionError 2": 
            messagebox.showerror(title="ZeroDivisionError (case 2)", message="ZeroDivisionError (case 2?): Make sure the y-value of Point 1 is > 0 when creating an exponential graph.")
            return
        if graph_parameters == "ValueError": 
            messagebox.showerror(title="ValueError", message="ValueError (math domain error): Make sure the y-value of Point 2 is >= 0 when creating an exponential graph.")
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
            if valuetwo < 0: 
                messagebox.showerror(title="ValueError", message="ValueError (math domain error): Make sure b-constant is >= 0 when creating an exponential graph.")
                return
        
    except ValueError:
        messagebox.showerror(title="ValueError", message="ValueError: Missing or invalid values.")
        return
    
    domain = (domain_start, domain_end)
    GraphGeneration((valueone, valuetwo), mode, domain)



def GraphGeneration(local_graph_parameters, local_mode, domain):
    global graph_parameters
    global mode
    graph_parameters = local_graph_parameters
    mode = local_mode
    plotpy.plt.close()
    plotpy.GenerateGraph(local_graph_parameters, mode, domain)
    InitTopLevelWindow()
    
    



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
















####################################################################################################################














def InvertInputs():
    global invert_inputs
    global plot_entry_one
    global plot_entry_two
    global plot_label_one
    global plot_label_two
    if invert_inputs.get():
        plot_label_one["text"] = "y"
        plot_label_two["text"] = "x"
    else:
        plot_label_one["text"] = "x"
        plot_label_two["text"] = "y"

    plot_entry_two["state"] = "normal"

    a = plot_entry_two.get()
    plot_entry_two.delete(0, tk.END)
    plot_entry_two.insert(0, plot_entry_one.get())

    plot_entry_one.delete(0, tk.END)
    plot_entry_one.insert(0, a)

    if lock_input.get(): 
        plot_entry_two["state"] = "readonly"

def UnlockInput():
    if lock_input.get():
        plot_entry_two["state"] = "readonly"
        CalculateEntryUpdate(graph_parameters, mode)
    else:
        plot_entry_two["state"] = "normal"

def CalculateEntryUpdate(graph_parameters, mode):
    # If 2nd Entry unlocked, don't do anything
    if not lock_input.get(): return
    
    # If not float, 2nd Entry becomes blank
    try: 
        value = float(plot_entry_one.get())
    except ValueError: 
        return_value = ""
        return EntryUpdate(return_value)

    #// TODO: Right now undefined only checks for x values. Fix. FIX: whatever lol. just let them plot along the line's gradient even if its not in the domain
    '''
    # Check to see which domain value is higher
    if domain[0] <= domain[1]: 
        # If not in domain, undefined
        if not (domain[0] <= value <= domain[1]):
            return_value = "N/A"
            return EntryUpdate(return_value)
    else:
         # If not in domain, undefined
         if not (domain[1] <= value <= domain[0]):
            return_value = "N/A"
            return EntryUpdate(return_value)
    '''
    
    #// TODO: Calculation is straight up wrong. FIX: Forgot to put brackets after .get() lol
    if mode == "Linear": # If Linear Graph
        if invert_inputs.get(): return_value = (value - graph_parameters[1])/graph_parameters[0] # Inverted
        else: return_value = (graph_parameters[0] * value) + graph_parameters[1] # Normal
    else: # If Expo Graph
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                if invert_inputs.get(): return_value = math.log((value/graph_parameters[0]), graph_parameters[1]) # Inverted
                else: return_value = graph_parameters[0] * np.power(graph_parameters[1], value) # Normal
        except ValueError: return_value = "N/A"


    round_to = str(value)[::-1].find('.')
    if round_to < 2:
        return_value = round(return_value, 2)
    else:
        return_value = round(return_value, round_to)
    return EntryUpdate(return_value)

    

def EntryUpdate(return_value):
    plot_entry_two["state"] = "normal"
    plot_entry_two.delete(0, tk.END)
    plot_entry_two.insert(0, return_value)
    plot_entry_two["state"] = "readonly"


def InitTopLevelWindow():
    # Amount of globals is horrendous lol
    global toplevel
    global title_entry_name
    global plot_label_one
    global plot_label_two
    global plot_entry_one
    global plot_entry_two
    global invert_inputs
    global lock_input

    try: toplevel.destroy()
    except: pass  
    toplevel = tk.Toplevel(root)
    toplevel.title("Plot Controls")
    toplevel.geometry("330x370")
    toplevel.resizable(False, False)
    
    invert_inputs = tk.BooleanVar()
    invert_inputs.set(False)
    lock_input = tk.BooleanVar()
    lock_input.set(True)


    # Create Frames
    frame_plot = tk.LabelFrame(toplevel, text="Plotting")
    frame_title = tk.LabelFrame(frame_plot, borderwidth=0)


    # Create Labels and Entries
    title_entry_name = tk.Entry(frame_title, width=15)

    plot_checkbox_invert = tk.Checkbutton(frame_plot, text="Swap", variable=invert_inputs, offvalue=False, onvalue=True, command=InvertInputs)
    plot_checkbox_lock = tk.Checkbutton(frame_plot, text="Lock 2nd Variable", variable=lock_input, offvalue=False, onvalue=True, command=UnlockInput)
    plot_label_one = tk.Label(frame_plot, text="x", anchor="center") 
    plot_label_two = tk.Label(frame_plot, text="y", anchor="center") 
    
    plot_entry_one = tk.Entry(frame_plot, width=7)
    plot_entry_two = tk.Entry(frame_plot, width=7, state="readonly")

    plot_button = tk.Button(frame_plot, text="Plot", height=2, width=10, bg="#f2c166", activebackground="#f2c166", command=lambda: plotpy.AddPointToDict(plot_entry_one.get(), plot_entry_two.get(), invert_inputs.get(), title_entry_name.get()))


    # Grid Frames
    frame_title.grid(row=0, column=0, columnspan=10, sticky="w")
    frame_plot.grid(row=1, column=0, sticky="w", padx=5)

    # Grid frame_title
    tk.Label(frame_title, text="Name (optional):").grid(row=0, column=0)
    title_entry_name.grid(row=0, column=1)

    # Grid frame_plot
    plot_checkbox_invert.grid(row=1, column=0, sticky="w")
    plot_label_one.grid(row=2, column=0, padx=0)
    plot_label_two.grid(row=2, column=1, padx=18, sticky="w") # Just has to be 18 to be centered
    plot_entry_one.grid(row=3, column=0, padx=0)
    plot_entry_two.grid(row=3, column=1, padx=0, sticky="w")

    plot_checkbox_lock.grid(row=3, column=2, sticky="w")

    plot_button.grid(row=3, column=9, rowspan=1, columnspan=3, sticky="e", padx=4, pady=4)
    
    plot_entry_one.bind("<KeyRelease>", lambda _: CalculateEntryUpdate(graph_parameters, mode))
    

    



    #tk.Button(frame_title, text='AAAAAAAAAAA', command=lambda: AddPointToDict(2, 3)).grid(row=0, column=1)




    toplevel.mainloop()

























ToggleInputTypes() # Run function to disable unselected entries
root.mainloop() # The Hog Rider card is unlocked from the Spell Valley (Arena 5). He is a very fast building-targeting, melee troop with moderately high hitpoints and damage. He appears just like his Clash of Clans counterpart; a man with brown eyebrows, a beard, a mohawk, and a golden body piercing in his left ear who is riding a hog. A Hog Rider card costs 4 Elixir to deploy.
