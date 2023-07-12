import math

def Find_a(point_one, b):
    return (point_one[1] * math.pow(b, -point_one[0]))

def Find_b(point_one, point_two):
    # NOTE: math.log's base dafault value is e.
    # NOTE: The formula is e^(ln(y1) - ln(y2)/x1 - x2)
    numerator = (math.log(point_one[1])-math.log(point_two[1])) #www.wolframalpha.com saves the day
    denominator = (point_one[0] - point_two[0])
    return math.pow(math.e, numerator/denominator) 
    
def CreateExponentialGraph(point_one, point_two):
    b = Find_b(point_one, point_two)
    a = Find_a(point_one, b)
    return (round(a, 8), round(b, 8)) # Prevent floating point shenanigans



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the calculation of a linear graph utilized by GraphGen.py
Please open GraphGen.py to access the graph generator.
(Any input will terminate this program)
""")

