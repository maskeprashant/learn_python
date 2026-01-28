import sys

def calc():
    
    if len(sys.argv) < 4:
        print("Invalid number of arguments")
        print("Enter <num1> <num2> <operator>")
        print("operator: + - * /")
        return
    
    if sys.argv[3] != "+" and sys.argv[3] != "-" and sys.argv[3] != "*" and sys.argv[3] != "/":
        print("Invalid operator")
        return

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operator = sys.argv[3]

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)

calc()