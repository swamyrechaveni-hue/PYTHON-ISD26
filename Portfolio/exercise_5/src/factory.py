import datetime
from tasks import Task, RecurringTask


class TaskFactory:
    @staticmethod
    def create_task(title: str, date: datetime.datetime, **kwargs):
        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])
        return Task(title, date)