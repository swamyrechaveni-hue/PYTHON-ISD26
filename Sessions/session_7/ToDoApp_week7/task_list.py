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

    def get_task(self, ix):
        if 0 <= ix < len(self.tasks):
            return self.tasks[ix]
        return None

    def view_tasks(self):
        print("Tasks to be completed:")
        for task in self.uncompleted_tasks:
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]