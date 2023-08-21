import tkinter as tk

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
    # if task_name:
    #     listbox.insert(tk.END, task_name)
    #     entry.delete(0, tk.END)

def add_task_to_list(task_name, is_important):
    listbox.insert(tk.END, task_name)
    if is_important:
        listbox.itemconfig(tk.END, {'fg': 'red'})


def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def print_selection():
    print("response" + str(important_checkbox_getter.get()))

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")

important_checkbox_getter = tk.IntVar()

# Create and configure widgets
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add_task_click)
delete_button = tk.Button(root, text="Delete", command=delete_task)
listbox = tk.Listbox(root)
important_checkbox = tk.Checkbutton(root, text="IMPORTANT", variable=important_checkbox_getter, onvalue=1, offvalue=0, command=print_selection)

# Arrange widgets using grid layout
entry.grid(row=0, column=0, padx=10, pady=10)
important_checkbox.grid(row=0, column=1, padx=0, pady=0)
add_button.grid(row=0, column=2, padx=10, pady=10)
delete_button.grid(row=1, column=1, padx=10, pady=10)
listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

# Start the Tkinter event loop
root.mainloop()
