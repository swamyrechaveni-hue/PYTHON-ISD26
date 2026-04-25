import datetime


class Task:
    def __init__(self, title: str, date_due: datetime.datetime):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def __str__(self) -> str:
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} | {status} | Due: {self.date_due.date()}"


class TaskList:
    def __init__(self, owner: str):
        self.owner = owner.upper()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        if 0 <= ix < len(self.tasks):
            del self.tasks[ix]
        else:
            print("Invalid index")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")