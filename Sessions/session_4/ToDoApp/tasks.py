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