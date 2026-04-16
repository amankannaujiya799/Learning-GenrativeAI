tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available right now.")
    else:
        print("\nYour To-Do Tasks:")
        count = 1
        for t in tasks:
            print(count, "->", t)
            count += 1


while True:

    print("\n Aman Bhai aap batao to shi kitne log ko add kar du")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("apni choice daal do bhai ab: ")

    if choice == "1":
        new_task = input("bhai turant task ka naam daal do: ")
        tasks.append(new_task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if len(tasks) > 0:
            remove_index = int(input("Enter task number to delete: "))
            
            if remove_index > 0 and remove_index <= len(tasks):
                removed = tasks.pop(remove_index - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number")

    elif choice == "4":
        print("Closing To-Do List App. Goodbye!")
        break

    else:
        print("Wrong choice Please select valid option.")