import matplotlib.pyplot as plt
import numpy as np

import _namelist as namelist

import tkinter as tk

def GenerateGraph(graph_parameters, mode, domain):
    
    plt.figure("Graph")
    plt.title(namelist.RandomTitle(mode))
    x = np.linspace(domain[0], domain[1])

    if mode == "Linear":
        y = LinGraph(graph_parameters, x)
    else:
        y = ExpGraph(graph_parameters, x)

    plt.plot(x, y)
    plt.ion()
    plt.show()

def LinGraph(graph_parameters, x):
    return (graph_parameters[0] * x) + graph_parameters[1] # y = mx+c

def ExpGraph(graph_parameters, x): # NOTE TO SELF: if you're gonna use numpy might as well just use numpy's methods instead of math's
    return graph_parameters[0] * np.power(graph_parameters[1], x) # y = ab^x


def InvertInputs():
    global plot_entry_two
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
    else:
        plot_entry_two["state"] = "normal"


def InitWindow():
    # Amount of globals is horrendous lol
    global root
    global plot_label_one
    global plot_label_two
    global plot_entry_one
    global plot_entry_two
    global invert_inputs
    global lock_input

    try: root.destroy()
    except: pass  
    root = tk.Tk()
    root.title("Plot Controls")
    root.geometry("380x370")
    root.resizable(False, False)
    
    invert_inputs = tk.BooleanVar()
    invert_inputs.set(False)

    lock_input = tk.BooleanVar()
    lock_input.set(True)




    # Create Frames
    frame_plot = tk.LabelFrame(root, text="Plotting")
    frame_title = tk.LabelFrame(frame_plot, borderwidth=0)


    # Create Labels and Entries
    title_entry_name = tk.Entry(frame_title, width=15)
    title_entry_color = tk.Entry(frame_title, width=7)

    plot_checkbox_invert = tk.Checkbutton(frame_plot, text="Swap", variable=invert_inputs, offvalue=False, onvalue=True, command=InvertInputs)
    plot_checkbox_lock = tk.Checkbutton(frame_plot, text="Lock 2nd Variable", variable=lock_input, offvalue=False, onvalue=True, command=UnlockInput)
    plot_label_one = tk.Label(frame_plot, text="x", anchor="center") 
    plot_label_two = tk.Label(frame_plot, text="y", anchor="center") 
    
    plot_entry_one = tk.Entry(frame_plot, width=7)
    plot_entry_two = tk.Entry(frame_plot, width=7, state="readonly")

    plot_button = tk.Button(frame_plot, text="Plot", height=2, width=10, bg="#f2c166", activebackground="#f2c166")


    # Grid Frames
    frame_title.grid(row=0, column=0, columnspan=10)
    frame_plot.grid(row=1, column=0, sticky="w", padx=5)

    # Grid frame_title
    tk.Label(frame_title, text="Name (optional):").grid(row=0, column=0)
    tk.Label(frame_title, text="Hex Color (optional):").grid(row=0, column=2)
    title_entry_name.grid(row=0, column=1)
    title_entry_color.grid(row=0, column=3, padx=5, sticky="nw")

    # Grid frame_plot
    plot_checkbox_invert.grid(row=1, column=0, sticky="w")
    plot_label_one.grid(row=2, column=0, padx=0)
    plot_label_two.grid(row=2, column=1, padx=18, sticky="w") # Just has to be 18 to be centered
    plot_entry_one.grid(row=3, column=0, padx=0)
    plot_entry_two.grid(row=3, column=1, padx=0, sticky="w")

    plot_checkbox_lock.grid(row=3, column=2, sticky="w")

    plot_button.grid(row=3, column=9, rowspan=1, columnspan=3, sticky="e", padx=4, pady=4)

    

    



    #tk.Button(frame_title, text='AAAAAAAAAAA', command=lambda: PlotPoint(2, 3)).grid(row=0, column=1)




    root.mainloop()

def PlotPoint(x, y):
    plt.scatter([x], [y])
    plt.text(x, y, f'lol\n({x}, {y})')




InitWindow() # ! Delete after testing



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the generation of the graph and the graph controls. Both of which are utilized by GraphGen.pyw
Please open GraphGen.pyw to access the graph generator.
(Any input will terminate this program)
""")
