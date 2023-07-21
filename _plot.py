import matplotlib.pyplot as plt
import numpy as np
import math

import _namelist as namelist

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

def PlotPoint(x, y):
    plt.scatter([x], [y])
    plt.text(x, y, f'lol\n({x}, {y})')




# InitWindow() # ! Delete after testing



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the generation of the graph and the graph controls. Both of which are utilized by GraphGen.pyw
Please open GraphGen.pyw to access the graph generator.
(Any input will terminate this program)
""")
