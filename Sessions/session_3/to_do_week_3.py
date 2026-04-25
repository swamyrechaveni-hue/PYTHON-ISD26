# Initialize an empty list to store tasks in memory during program execution
tasks = []


def add_task():
    """
    Prompts the user to enter a task and appends it to the global tasks list.
    Provides simple confirmation after adding.
    """
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")


def view_tasks():
    """
    Displays all current tasks.
    Handles the case where the task list is empty to avoid unnecessary iteration.
    """
    if not tasks:
        print("No tasks available.")
    else:
        # Enumerate provides indexed display starting from 1 for user readability
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task():
    """
    Removes a task based on exact match input from the user.
    Validates existence before attempting removal to prevent runtime errors.
    """
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")


# Main program loop: continuously prompts user until exit condition is met
while True:
    print("To-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    # Accept user input for menu selection
    choice = input("Enter your choice: ")

    # Conditional branching based on user selection
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        # Graceful termination of program loop
        print("Exiting program.")
        break
    else:
        # Input validation for unexpected values
        print("Invalid choice. Please try again.")