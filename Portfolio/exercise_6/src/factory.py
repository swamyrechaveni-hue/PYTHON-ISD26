import datetime
from tasks import Task, RecurringTask, PriorityTask


class TaskFactory:
    @staticmethod
    def create_task(title, date, **kwargs):

        if "priority" in kwargs:
            return PriorityTask(title, date, kwargs["priority"])

        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])

        return Task(title, date)