# Calculator function
# Clean the function - a function should only do ONE thing
# Write tests
# Implement substraction and multiplication
# for multiplication allow operators to be x,X or *

def calc(num1: int, num2: int, op: str) -> int|str:  # returns integers or strings
    """
    Function to calculate
    Parameters:
        num1 = number
        num2 = number
        op = string which is +, =, /, x/X, *
    """
    try:
        if op == "+":
            return num1+num2
        if op == "/":
            if num2 == 0:
                return "Zero Division not possible"
            return num1/num2
        if op in "xX*":
            return num1 * num2
        return "Operation not allowed"
    except Exception as e:
        return f"**** ERROR: {e}"
    # print(res); don't need a print, we want a return
    # return res

def log_this(to_log: str) -> None:  
    """
    Function to log to file log.txt
    Parameters:
        to_log: String to log
    """
    # f = open("log.txt", "+a")
    # log_txt = f"6+2={res}\n"
    # f.write(log_txt)
    # return res
    # the above is not recommended in Python - it is UNCLEAN; clean code says to remove the comments so people can understand what's going on
    with open("log.txt", "+a") as file_pointer:
        file_pointer.write(to_log)

print(f"6+2={calc(6, 2, "+")}")
print(f"6/2={calc(6, 2, "/")}")
# print(f"6+2={calc('6', 2, "+")}")
# print(f"6-2={calc(6, 2, "-")}")
# print(f"6*2={calc(6, 2, "x")}")
# print(f"6*2={calc(6, 2, "d")}")