tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                print(i, "-", task)

    elif choice == "3":
        index = int(input("Enter task number to remove: "))
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print("Removed:", removed)
        else:
            print("Invalid index")

    elif choice == "4":
        break

    else:
        print("Invalid choice")