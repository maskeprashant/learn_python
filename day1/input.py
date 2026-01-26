def main():
    print("This is the main function.")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    skills = input("Enter your skills (comma separated): ")

    skills_arr = skills.split(",")

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Skills:")

    for skill in skills_arr:
        print(f"- {skill.strip()}")

main()