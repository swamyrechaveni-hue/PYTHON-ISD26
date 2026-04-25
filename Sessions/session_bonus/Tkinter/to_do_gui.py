import tkinter as tk

tasks = []


def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def remove_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        listbox.delete(index)
        tasks.pop(index)


root = tk.Tk()
root.title("To Do List")

entry = tk.Entry(root)
entry.pack()

listbox = tk.Listbox(root)
listbox.pack()

tk.Button(root, text="Add", command=add_task).pack()
tk.Button(root, text="Remove", command=remove_task).pack()

root.mainloop()