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

def InitWindow():
    global root
    try: root.destroy()
    except: pass  
    root = tk.Tk()
    root.title("Graph Controls")
    root.geometry("380x370")
    root.resizable(False, False)

    # Create Frames
    frame_title = tk.LabelFrame(root, borderwidth=0)
    frame_plotline = tk.LabelFrame(root, borderwidth=0)

    # Create Labels and Entries
    title_entry_name = tk.Entry(frame_title, width=16)
    title_entry_color = tk.Entry(frame_title, width=9)

    # Grid Frames
    frame_title.grid(row=0, column=0)
    frame_plotline.grid(row=0, column=1)

    # Grid Labels and Entries
    tk.Label(frame_title, text="Name (optional):").grid(row=0, column=0)
    tk.Label(frame_title, text="Hex Color (optional):").grid(row=0, column=2)
    title_entry_name.grid(row=0, column=1)
    title_entry_color.grid(row=0, column=3)
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
