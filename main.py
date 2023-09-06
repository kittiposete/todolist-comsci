for i in range(2):
    try:
        import tkinter as tk
        from task_item import TaskItem
        import database
        import tkcalendar
        import datetime

        break
    except ModuleNotFoundError:
        import install_pip

        install_pip.install_pip()

task_list = []


def add_task_click():
    task_name = entry.get()
    if task_name == "" or task_name is None:
        return
    is_important_int = important_checkbox_getter.get()
    is_important = None
    if is_important_int == 0:
        is_important = False
    elif is_important_int == 1:
        is_important = True
    else:
        Exception("Error: get data from checkbox")

    # get date from date picker
    date = date_picker.get_date()
    date = date.split("/")
    month = date[0]
    day = date[1]
    year = date[2]
    year = "20" + year

    # convent to int
    date_object = datetime.date(int(year), int(month), int(day))
    date_int = date_object.toordinal()
    print("date_int : %d" % date_int)

    if task_name:
        add_task_to_list(TaskItem(task_name, is_important, date_int))


def add_task_to_list(task: TaskItem):
    task_name = task.task_title
    is_important = task.is_important
    date = task.date
    date_object = datetime.date.fromordinal(date)
    date_string = date_object.strftime("%d/%m/%Y")

    listbox.insert(tk.END, "%s - %s" % (task_name, date_string))
    task_list.append(task)
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

# set window size
root.geometry("600x400")

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

# Arrange widgets using space left and top
listbox.place(x=0, y=0, width=200, height=200)
delete_button.place(x=0, y=200, width=100, height=30)

entry.place(x=250, y=0, width=200, height=30)
add_button.place(x=250, y=60, width=100, height=30)
important_checkbox.place(x=250, y=30, width=100, height=30)
save_button.place(x=0, y=240, width=100, height=30)
date_picker.place(x=250, y=100, width=200, height=200)

disk_data = database.load_from_disk()
if disk_data is not None:
    for item in disk_data:
        is_important = item["is_important"]
        task_name = item["task_title"]
        add_task_to_list(TaskItem(task_name, is_important, 0))

# Start the Tkinter event loop
root.mainloop()
