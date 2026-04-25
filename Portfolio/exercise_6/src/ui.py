import datetime
from controllers import TaskManagerController


class CommandLineUI:
    def __init__(self):
        self.controller = TaskManagerController("User")

    def _print_menu(self):
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark completed")
        print("5. Change title")
        print("6. Quit")
        print("7. Load tasks")
        print("8. Save tasks")

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter choice: ")

            try:
                if choice == "1":
                    print("Task type: 1-Normal 2-Recurring 3-Priority")
                    task_type = input("Choose type: ")

                    title = input("Enter task: ")
                    date = datetime.datetime.strptime(
                        input("Enter date (DD/MM/YYYY): "), "%d/%m/%Y"
                    )

                    if task_type == "2":
                        days = int(input("Interval days: "))
                        interval = datetime.timedelta(days=days)
                        self.controller.add_task(title, date, interval)

                    elif task_type == "3":
                        priority = int(input("Priority (1-3): "))
                        self.controller.add_task(title, date, priority=priority)

                    else:
                        self.controller.add_task(title, date)

                elif choice == "2":
                    tasks = self.controller.view_tasks()
                    for t in tasks:
                        print(t)

                elif choice == "3":
                    ix = int(input("Index: "))
                    self.controller.remove_task(ix)

                elif choice == "4":
                    ix = int(input("Index: "))
                    self.controller.mark_completed(ix)

                elif choice == "5":
                    ix = int(input("Index: "))
                    title = input("New title: ")
                    self.controller.change_title(ix, title)

                elif choice == "7":
                    path = input("CSV path: ")
                    self.controller.load_tasks(path)

                elif choice == "8":
                    path = input("CSV path: ")
                    self.controller.save_tasks(path)

                elif choice == "6":
                    break

                else:
                    print("Invalid choice")

            except IndexError:
                print("Invalid index. Try again.")
            except Exception as e:
                print("Error:", e)