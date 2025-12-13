# To-Do List

tasks = []

while True:
    print("\nTo Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully")

    elif choice == 2:
        print("Your Tasks:")
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for t in tasks:
                print("-", t)

    elif choice == 3:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(i, tasks[i])

        d = int(input("Enter index to delete: "))
        tasks.pop(d)
        print("Task deleted!")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
