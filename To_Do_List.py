# Simple To-Do List in Python with Completed Feature

# Start with an empty list to store tasks
tasks = []

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = " (Completed)" if task[1] else ""
            print(f"{i}. {task[0]}{status}")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append([task, False])
    print(f"Task '{task}' added.")

# Function to update a task
def update_task():
    display_tasks()
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num][0] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    display_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed():
    display_tasks()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num][1] = True
        print(f"Task '{tasks[task_num][0]}' marked as completed.")
    else:
        print("Invalid task number.")

# Main loop to handle user input
while True:
    print("\nMenu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_completed()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")