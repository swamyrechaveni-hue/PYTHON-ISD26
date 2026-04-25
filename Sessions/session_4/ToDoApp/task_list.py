from tasks import Task


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