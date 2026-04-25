import csv
import datetime
from tasks import Task, RecurringTask, PriorityTask


class TaskCsvDAO:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.fieldnames = [
            "title", "type", "date_due", "completed",
            "interval", "completed_dates", "date_created", "priority"
        ]

    def get_all_tasks(self):
        task_list = []

        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = row["title"]
                task_type = row["type"]

                date_due = datetime.datetime.strptime(row["date_due"], "%d/%m/%Y")
                completed = row["completed"].upper() == "TRUE"

                if task_type == "RecurringTask":
                    interval_days = int(row["interval"].split()[0])
                    interval = datetime.timedelta(days=interval_days)

                    task = RecurringTask(title, date_due, interval)

                    if row["completed_dates"]:
                        dates = row["completed_dates"].split(",")
                        task.completed_dates = [
                            datetime.datetime.strptime(d.strip(), "%Y-%m-%d")
                            for d in dates
                        ]

                elif task_type == "PriorityTask":
                    priority = int(row["priority"])
                    task = PriorityTask(title, date_due, priority)

                else:
                    task = Task(title, date_due)

                task.completed = completed
                task.date_created = datetime.datetime.strptime(
                    row["date_created"], "%d/%m/%Y"
                )

                task_list.append(task)

        return task_list

    def save_all_tasks(self, tasks):
        with open(self.storage_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

            for task in tasks:
                row = {}

                row["title"] = task.title
                row["date_due"] = task.date_due.strftime("%d/%m/%Y")
                row["completed"] = str(task.completed).upper()
                row["date_created"] = task.date_created.strftime("%d/%m/%Y")

                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                    row["interval"] = f"{task.interval.days} days"
                    row["completed_dates"] = ",".join(
                        d.strftime("%Y-%m-%d") for d in task.completed_dates
                    )
                    row["priority"] = ""

                elif isinstance(task, PriorityTask):
                    row["type"] = "PriorityTask"
                    row["priority"] = str(task.priority)
                    row["interval"] = ""
                    row["completed_dates"] = ""

                else:
                    row["type"] = "Task"
                    row["interval"] = ""
                    row["completed_dates"] = ""
                    row["priority"] = ""

                writer.writerow(row)