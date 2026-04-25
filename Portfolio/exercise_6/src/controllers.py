import datetime
from task_list import TaskList
from factory import TaskFactory
from dao import TaskCsvDAO


class TaskManagerController:
    def __init__(self, owner: str):
        self.task_list = TaskList(owner)

    def add_task(self, title, date, interval=None):
        if interval:
            task = TaskFactory.create_task(title, date, interval=interval)
        else:
            task = TaskFactory.create_task(title, date)

        self.task_list.add_task(task)

    def view_tasks(self):
        return self.task_list.uncompleted_tasks

    def remove_task(self, ix):
        if self.task_list.check_task_index(ix):
            self.task_list.remove_task(ix)
        else:
            raise IndexError("Invalid index")

    def mark_completed(self, ix):
        if self.task_list.check_task_index(ix):
            self.task_list.tasks[ix].mark_completed()
        else:
            raise IndexError("Invalid index")

    def change_title(self, ix, title):
        if self.task_list.check_task_index(ix):
            self.task_list.tasks[ix].change_title(title)
        else:
            raise IndexError("Invalid index")

    def load_tasks(self, path):
        dao = TaskCsvDAO(path)
        tasks = dao.get_all_tasks()
        for t in tasks:
            self.task_list.add_task(t)

    def save_tasks(self, path):
        dao = TaskCsvDAO(path)
        dao.save_all_tasks(self.task_list.tasks)