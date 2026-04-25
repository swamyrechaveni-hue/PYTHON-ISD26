import datetime


class Task:
    """
    Represents a single task with a title, completion status,
    creation timestamp, and a due date.
    """
    def __init__(self, title: str, date_due: datetime.datetime):
        # Initialize task attributes at creation
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

    def mark_completed(self) -> None:
        """
        Updates the task status to completed.
        """
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """
        Allows modification of the task title.
        """
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        """
        Updates the due date of the task.
        """
        self.date_due = date_due

    def __str__(self) -> str:
        """
        Provides a readable string representation of the task,
        including status and due date.
        """
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} | {status} | Due: {self.date_due.date()}"


class TaskList:
    """
    Manages a collection of Task objects associated with a specific owner.
    Provides operations to add, remove, and view tasks.
    """
    def __init__(self, owner: str):
        # Store owner name in uppercase for consistency
        self.owner = owner.upper()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Adds a new Task object to the task list.
        """
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """
        Removes a task based on its index.
        Includes bounds checking to prevent invalid access.
        """
        if 0 <= ix < len(self.tasks):
            del self.tasks[ix]
        else:
            print("Invalid index")

    def view_tasks(self) -> None:
        """
        Displays all tasks with their index positions.
        Handles empty list scenario gracefully.
        """
        if not self.tasks:
            print("No tasks available")
        else:
            # Enumerate provides index for reference during removal or updates
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")