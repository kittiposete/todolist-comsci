import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")

# Create and configure widgets
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add_task)
delete_button = tk.Button(root, text="Delete", command=delete_task)
listbox = tk.Listbox(root)

# Arrange widgets using grid layout
entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
delete_button.grid(row=1, column=1, padx=10, pady=10)
listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

# Start the Tkinter event loop
root.mainloop()
