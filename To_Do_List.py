import os  # Import to check if the file exists

TASKS_FILE = "tasks.txt"  # Name of the file where tasks will be saved

def load_tasks():
    """Load tasks from a file if it exists."""
    if not os.path.exists(TASKS_FILE):
        return []  # Return an empty list if no file exists
    
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)  # Save the updated task list to file
        print(f"✅ Task added: {task}")
    else:
        print("❌ Task cannot be empty!")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)  # Save the updated task list to file
            print(f"🗑️ Task removed: {removed_task}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()  # Load tasks at the start
    
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
