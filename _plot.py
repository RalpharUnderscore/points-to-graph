import matplotlib.pyplot as plt
import numpy as np

import _namelist as namelist
import _gen as graphgen

from tkinter import messagebox
PLOTDICT = {}

def GenerateGraph(local_graph_parameters, local_mode, local_domain, local_name):
    # writes unmaintainable code
    global graph_parameters
    global mode
    global domain
    global name
    graph_parameters = local_graph_parameters    
    mode = local_mode    
    domain = local_domain
    name = local_name    
    
    plt.figure("Graph")
    plt.title(name)
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

def AddPointToDict(entryone, entrytwo, invert, name):
    try:
        if invert:
            y = float(entryone)
            x = float(entrytwo)
        else:
            x = float(entryone)
            y = float(entrytwo)
    except ValueError:
        messagebox.showerror(title="ValueError", message="ValueError: Missing or invalid values.")
        return
    
    if name == "":
        name = namelist.RandomName()

    while name in PLOTDICT:
        name = f"{name} Jr."

    PLOTDICT[name] = (x, y)
    UpdatePoints()
    

def UpdatePoints():
    #// ! Program crashes with no error message FIX: opted for plt.cla()
    plt.cla()
    GenerateGraph(graph_parameters, mode, domain, name)

    X_VAL_LIST = []
    Y_VAL_LIST = []

    for value in PLOTDICT.values():
        X_VAL_LIST.append(value[0])
        Y_VAL_LIST.append(value[1])
        
    plt.scatter(X_VAL_LIST, Y_VAL_LIST)
    
    for key, value in PLOTDICT.items():
        plt.text(value[0], value[1], f'\n{key}\n({value[0]}, {value[1]})', horizontalalignment='left', verticalalignment='top', fontsize=9) # ? my honest reaction when 'left' 'top' aligns it 'right' 'bottom' 



# InitWindow() # ! Delete after testing 



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the generation of the graph and plotting utilized by GraphGen.pyw
Please open GraphGen.pyw to access the graph generator.
(Any input will terminate this program)
""")
