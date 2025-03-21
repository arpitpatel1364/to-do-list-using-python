def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks):
        status = "✔️" if task['completed'] else "❌"
        print(f"{index + 1}. {task['description']} [{status}]")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_description = input("Enter new task description: ")
        tasks[task_number]['description'] = new_description
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_completed(tasks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()