import math

def Find_c(point_one, m):
    return point_one[1] - (m * point_one[0])

def Find_m(point_one, point_two):
    # The formula for gradient is (y2-y1)/(x2-x1)
    numerator = point_two[1] - point_one[1]
    denominator = point_two[0] - point_one[0]
    try:
        return numerator/denominator
    except ZeroDivisionError:
        return "Error"
    
def CreateLinearGraph(point_one, point_two):
    m = Find_m(point_one, point_two)
    if m != "Error":
        c = Find_c(point_one, m)
        return (round(m, 8), round(c, 8)) # Prevent floating point shenanigans
    else:
        return "Error"
    



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the calculation of a linear graph utilized by GraphGen.py
Please open GraphGen.py to access the graph generator.
(Any input will terminate this program)
""")

