def create_file():
    file = open("tasks.txt", "w")

def count_lines():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0

def delete_task():
    task_num = int(input("Enter task number to delete: "))
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 0 < task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")
        return

def done_task():
    pass

def search_task():
    pass

def summery_task():
    pass


def list_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("nothing to show")
            for idx, task in enumerate(tasks, start=1):
                print(f"{task.strip()}")
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

def add_task():
    task = input("Enter task to add: ")
    count = count_lines()
    with open("tasks.txt", "a") as file:
        file.write(f"[ {count + 1} ] - {task} \n")
    print("Task added.")
    list_tasks()

def main():
    print("Choose action to perform:")
    user = input(f"1) Add  2) Delete 3) Done 4) Search 5) List 6) Summery 0) Exit \n")
    if user == "1":
        print("Add Contact")
        add_task()
    elif user == "2":
        print("Delete Contact")
        delete_task()
    elif user == "3":
        print("Done Contact")
    elif user == "4":
        print("Search Contact")
    elif user == "5":
        print("List Contact")
        list_tasks()
    elif user == "6":
        print("Summery Contact")
    elif user == "0":
        print("Exit")
    else:
        print("Invalid Input")

main()