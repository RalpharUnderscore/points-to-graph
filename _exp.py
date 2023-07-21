import math

def Find_a(point_one, b):
    return (point_one[1] * math.pow(b, -point_one[0]))

def Find_b(point_one, point_two):
    # NOTE: Updated calculation from the old version: b = e^((ln(y1) - ln(y2))/(x1 - x2))
    # which I used wolframalpha.com to find
    # To new version: b = (y2/y1)^(1/(x2-x1))
    # While it has less efficiency in time complexity at least came up with it (with a tiny bit of help from ChatGPT)

    try: 
        #//numerator = (math.log(point_one[1])-math.log(point_two[1])) #www.wolframalpha.com saves the day
        numerator = (point_two[1]/point_one[1])
    except ZeroDivisionError: 
        return "ZeroDivisionError 2"
    #//denominator = (point_one[0] - point_two[0])
    denominator = (point_two[0] - point_one[0])


    # return math.pow(math.e, numerator/denominator)
    #//return math.pow(math.e, numerator/denominator)
    try:
        return math.pow(numerator, 1/denominator)
    except (ZeroDivisionError, ValueError) as issue:
        if isinstance(issue, ZeroDivisionError):
            return "ZeroDivisionError" 
        else:
            return "ValueError"
    
def CreateExponentialGraph(point_one, point_two):
    b = Find_b(point_one, point_two)
    if isinstance(b, float):
        a = Find_a(point_one, b)
        return (round(a, 8), round(b, 8)) # Prevent floating point shenanigans
    else:
        return b
    



if __name__ == "__main__":
    input("""This Python file does nothing when executed by the user.
It contains the code for the calculation of a linear graph utilized by GraphGen.pyw
Please open GraphGen.pyw to access the graph generator.
(Any input will terminate this program)
""")

