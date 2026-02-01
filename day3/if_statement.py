# simple if statement to check age
age = int(input("Enter your age: "))

if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# nested if statement to check grade

marks = int(input("Enter your marks:"))

if marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


