
name =input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
skills_input = input("Enter your skills: (use comma separated) ")

skills = skills_input.split(",")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Skills: {skills}")

