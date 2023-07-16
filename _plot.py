import matplotlib.pyplot as plt
import numpy as np

def GenerateGraph(graph_parameters, mode, domain):
    
    plt.figure("My Graph")
    plt.title(f"Untitled {mode} Graph")
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


if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the generation of the graph utilized by GraphGen.py
Please open GraphGen.py to access the graph generator.
(Any input will terminate this program)
""")
