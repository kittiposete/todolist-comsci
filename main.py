import install_pip

install_pip.install_pip()

import tkinter as tk
from task_item import TaskItem
import database
import tkcalendar

task_list = []


def add_task_click():
    task_name = entry.get()
    is_important_int = important_checkbox_getter.get()
    is_important = None
    if is_important_int == 0:
        is_important = False
    elif is_important_int == 1:
        is_important = True
    else:
        Exception("Error: get data from checkbox")

    if task_name:
        add_task_to_list(task_name, is_important)


def add_task_to_list(task_name, is_important):
    listbox.insert(tk.END, task_name)
    task_list.append(TaskItem(task_name, is_important, 0))
    if is_important:
        listbox.itemconfig(tk.END, {'fg': 'red'})


def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index[0])
        task_list.pop(selected_task_index[0])


def print_selection():
    print("response" + str(important_checkbox_getter.get()))


def save():
    database.save_to_disk(task_list)


# Create the main application window
root = tk.Tk()
root.title("To-Do List App")

important_checkbox_getter = tk.IntVar()

# Create and configure widgets
listbox = tk.Listbox(root)
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add_task_click)
important_checkbox = tk.Checkbutton(root, text="IMPORTANT", variable=important_checkbox_getter,
                                    onvalue=1, offvalue=0,
                                    command=print_selection)
delete_button = tk.Button(root, text="Delete", command=delete_task)
save_button = tk.Button(root, text="save", command=save)
date_picker = tkcalendar.Calendar(root, selectmode="day")

# Arrange widgets using grid layout
listbox.grid(row=0, column=0, columnspan=2, sticky="nsew")
delete_button.grid(row=1, column=0, sticky="nsew")

entry.grid(row=0, column=1, sticky="nsew")
important_checkbox.grid(row=1, column=1, sticky="nsew")
add_button.grid(row=1, column=0, sticky="nsew")
save_button.grid(row=1, column=1, sticky="nsew")

disk_data = database.load_from_disk()
if disk_data is not None:
    for item in disk_data:
        is_important = item["is_important"]
        task_name = item["task_title"]
        add_task_to_list(task_name, is_important)

# Start the Tkinter event loop
root.mainloop()
