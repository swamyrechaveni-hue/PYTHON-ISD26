from task_list import TaskList
from tasks import Task, RecurringTask
import datetime


def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", datetime.datetime.now()))
    task_list.add_task(Task("Do laundry", datetime.datetime.now()))
    task_list.add_task(Task("Clean room", datetime.datetime.now()))
    return task_list


def main() -> None:
    task_list = TaskList("Your Name")
    task_list = propagate_task_list(task_list)

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark completed")
        print("5. Change title")
        print("6. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            choice = input("Add recurring task? (y/n): ")
            title = input("Enter task: ")
            date_input = input("Enter due date (YYYY-MM-DD): ")
            date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

            if choice.lower() == "y":
                interval_days = int(input("Enter interval in days: "))
                interval = datetime.timedelta(days=interval_days)
                task = RecurringTask(title, date_obj, interval)
            else:
                task = Task(title, date_obj)

            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Enter index: "))
            task_list.remove_task(ix)

        elif choice == "4":
            ix = int(input("Enter index: "))
            if 0 <= ix < len(task_list.tasks):
                task_list.get_task(ix).mark_completed()

        elif choice == "5":
            ix = int(input("Enter index: "))
            new_title = input("Enter new title: ")
            if 0 <= ix < len(task_list.tasks):
                task_list.get_task(ix).change_title(new_title)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()