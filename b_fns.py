# Calculator function
# Clean the function
# Write tests
# Implement substraction and multiplication
# for multiplication allow operators to be x,X or *

def calc(num1, num2, op):
    r = ""
    if op == "+":
        res = num1+num2
    elif op == "/":
        res = num1/num2
    else:
        res = "Operation not allowed"
    print(res)
    f = open("log.txt", "+a")
    log_txt = f"6+2={res}\n"
    f.write(log_txt)
    return res

print(f"6+2={calc(6, 2, "+")}")
print(f"6/2={calc(6, 2, "/")}")
# print(f"6+2={calc('6', 2, "+")}")
# print(f"6-2={calc(6, 2, "-")}")
# print(f"6*2={calc(6, 2, "x")}")
# print(f"6*2={calc(6, 2, "d")}")