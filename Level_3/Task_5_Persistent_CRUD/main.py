
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if isinstance(tasks, list) and all(
            isinstance(task, str) for task in tasks
        ):
            return tasks

        print("Warning: Invalid task data. Starting with an empty list.")
        return []

    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load tasks: {error}")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
        return True
    except OSError as error:
        print(f"Could not save tasks: {error}")
        return False


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks):
    task = input("Enter the task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)

    if save_tasks(tasks):
        print("Task added and saved successfully!")
    else:
        tasks.pop()


def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return

        new_task = input("Enter the updated task: ").strip()

        if not new_task:
            print("Task cannot be empty.")
            return

        old_task = tasks[number - 1]
        tasks[number - 1] = new_task

        if save_tasks(tasks):
            print("Task updated successfully!")
        else:
            tasks[number - 1] = old_task

    except ValueError:
        print("Please enter a valid whole number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)

        if save_tasks(tasks):
            print(f"Deleted task: {removed_task}")
        else:
            tasks.insert(number - 1, removed_task)

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    tasks = load_tasks()
    print("===== PERSISTENT TASK MANAGER =====")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
