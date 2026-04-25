tasks = []


def add_task(lst):
    lst.append(input("Add a task: "))


def view_tasks(lst):
    count = 0
    for element in lst:
        print(f"{count + 1}.{element}")
        count += 1
    print("Total tasks:", len(lst))


def remove_task(lst):
    choice = int(input("Task number to remove: ")) - 1
    if choice not in range(len(lst)):
        print("Invalid task number.")
        return
    lst.pop(choice)


def main():
    while True:
        print("1. Add")
        print("2. View")
        print("3. Remove")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()