import sys

class InvalidOperatorError(Exception):
    """Raised when an invalid operator is provided, see errors.log for details"""
    pass


class InvalidArguments(Exception):
    """Raised when invalid number or type of arguments are provided, see errors.log for details"""
    pass

def safe_calculator(num1, num2, operator):
    try:

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise InvalidArguments("Arguments must be numbers")

        if operator not in ["+", "-", "*", "/"]:
            raise InvalidOperatorError(f"Invalid operator: {operator}")

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise InvalidArguments("Division by zero is not allowed")
            return num1 / num2
    except (InvalidOperatorError, InvalidArguments) as e:
        with open("errors.log", "a") as log_file:
            log_file.write(f"{str(e)}\n")
        return "Error occurred. Check errors.log for details."

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    result = safe_calculator(num1, num2, operation)
    print(f"Result: {result}")
    print("Thank you for using safe_calc")

main()