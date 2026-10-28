
tasks = []


def add_task():
    task = input("Enter the task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ").strip()

            if new_task:
                tasks[task_number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid whole number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    while True:
        print("\n===== CONSOLE TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using Task Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
