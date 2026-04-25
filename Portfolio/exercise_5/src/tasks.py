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

class RecurringTask(Task):
    def __init__(self, title, date_due, interval):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates = []

    def _compute_next_due_date(self):
        return self.date_due + self.interval

    def mark_completed(self):
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self):
        return f"{self.title} (Recurring, next due: {self.date_due}, interval: {self.interval})"