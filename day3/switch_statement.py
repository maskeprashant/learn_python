# learn python switch statement example

day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Please enter number between 1 to 7")


# Example of switch statement to perform basic arithmetic operations

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    match operator:
        case "+":
            print(f" {num1} + { num2 } = {num1 + num2}")
            
        case "-":
            print(f" {num1} - { num2 } = { num1 - num2}")
        
        case "*":
            print(f" {num1} * { num2 } = {num1 * num2}")
        
        case "/":
            if num2 != 0:
                print(f" {num1} / {num2} = { num1 / num2}")
            else:
                print("Error: Division by zero")
        case _:
            print("Invalid operator")
    cont = input("Do you want to perform another operation? (yes/no): ")
    if cont.lower() != "yes":
        break