tasks = []

def view_tasks():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    count = 1

    for task in tasks:

        if task["completed"] == True:
            status = "[x]"
        else:
            status = "[ ]"

        print(str(count) + ". " + status + " " + task["description"])

        count += 1

def add_task():

    description = input("Enter task description: ")

    if description == "":
        print("Task cannot be empty.")
        return

    new_task = {
        "description": description,
        "completed": False
    }

    tasks.append(new_task)

    print("Task added successfully.")

def mark_task_complete():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    number = input("Enter task number to mark complete: ")

    if number.isdigit():

        number = int(number)

        if number >= 1 and number <= len(tasks):

            tasks[number - 1]["completed"] = True

            print("Task marked as completed.")

        else:
            print("Invalid task number.")

    else:
        print("Please enter a valid number.")


def delete_task():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    number = input("Enter task number to delete: ")

    if number.isdigit():

        number = int(number)

        if number >= 1 and number <= len(tasks):

            tasks.pop(number - 1)

            print("Task deleted successfully.")

        else:
            print("Invalid task number.")

    else:
        print("Please enter a valid number.")

while True:

    print("\n----- TO DO LIST MENU -----")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        mark_task_complete()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Try again.")