for i in range(2):
    try:
        import tkinter as tk
        from task_item import TaskItem
        import database
        import tkcalendar
        import datetime
        import PIL
        import PIL.Image
        import sort_mode

        break
    except ModuleNotFoundError:
        import install_pip

        install_pip.install_pip()


class Application:
    def resort_tasklist(self):
        new_task_list1 = []
        if self.sort_mode == sort_mode.SortMode().name:
            # sort by name
            new_task_list1 = sorted(self.task_list, key=lambda task: task.task_title)
        elif self.sort_mode == sort_mode.SortMode().date:
            # sort by date
            new_task_list1 = sorted(self.task_list, key=lambda task: task.date)
        else:
            Exception("Error: sort mode")

        # move finished task to the end of list
        new_task_list2 = []
        for task in new_task_list1:
            if not task.is_finished:
                new_task_list2.append(task)
        for task in new_task_list1:
            if task.is_finished:
                new_task_list2.append(task)
        self.task_list = new_task_list2

    def reload_listbox(self):
        self.resort_tasklist()
        print("run reload listbox")
        # clear listbox
        self.listbox.delete(0, tk.END)
        print("clear listbox")
        # add task to listbox
        print(self.task_list)
        # breakpoint()
        task_list_size = len(self.task_list)
        for index in range(task_list_size):
            self.add_task_to_list_ui(self.task_list[index])

    def add_task_click(self):
        task_name = self.entry.get()
        if task_name == "" or task_name is None:
            return
        is_important_int = self.important_checkbox_getter.get()
        is_important = None
        if is_important_int == 0:
            is_important = False
        elif is_important_int == 1:
            is_important = True
        else:
            Exception("Error: get data from checkbox")

        # get date from date picker
        date = self.date_picker.get_date()
        date = date.split("/")
        month = date[0]
        day = date[1]
        year = date[2]
        year = "20" + year

        # convent to int
        date_object = datetime.date(int(year), int(month), int(day))
        date_int = date_object.toordinal()
        print("date_int : %d" % date_int)

        # create task item
        task_item = TaskItem(task_name, is_important, date_int)
        self.task_list.append(task_item)
        self.reload_listbox()

    def add_task_to_list_ui(self, task: TaskItem):
        task_name = task.task_title
        is_important = task.is_important
        is_finished = task.is_finished
        date = task.date
        date_object = datetime.date.fromordinal(date)
        date_string = date_object.strftime("%d/%m/%Y")

        if is_finished:
            self.listbox.insert(tk.END, "%s - Finished" % task_name)
            self.listbox.itemconfig(tk.END, {'fg': 'grey'})
        else:
            self.listbox.insert(tk.END, "%s - %s" % (task_name, date_string))
            if is_important:
                self.listbox.itemconfig(tk.END, {'fg': 'red'})
            else:
                self.listbox.itemconfig(tk.END, {'fg': 'black'})

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.task_list.pop(selected_task_index[0])
            self.reload_listbox()

    def save(self):
        database.save_to_disk(self.task_list)

    def finish_task(self):
        print("run finish task")
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.task_list[selected_task_index[0]].is_finished = True
            print("add finish task")
            # refresh listbox
            self.reload_listbox()
            print("reload listbox")

    def sort_by_name(self):
        self.sort_mode = sort_mode.SortMode().name
        self.reload_listbox()

    def sort_by_date(self):
        self.sort_mode = sort_mode.SortMode().date
        self.reload_listbox()

    def __init__(self):
        self.task_list = []

        # Create the main application window
        root = tk.Tk()
        root.title("To-Do List App")

        # set window size
        root.geometry("600x400")

        self.important_checkbox_getter = tk.IntVar()
        self.sort_mode = sort_mode.SortMode().name

        # Create and configure widgets
        self.listbox = tk.Listbox(root)
        self.entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add", command=self.add_task_click)
        self.important_checkbox = tk.Checkbutton(root, text="IMPORTANT", variable=self.important_checkbox_getter,
                                                 onvalue=1, offvalue=0)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.save_button = tk.Button(root, text="save", command=self.save)
        self.finish_button = tk.Button(root, text="finish", command=self.finish_task)
        self.date_picker = tkcalendar.Calendar(root, selectmode="day")
        self.sort_by_label = tk.Label(root, text="Sort by:")
        self.sort_by_name_button = tk.Button(root, text="Name", command=self.sort_by_name)
        self.sort_by_date_button = tk.Button(root, text="Date", command=self.sort_by_date)

        # Arrange widgets using space left and top
        self.listbox.place(x=0, y=50, width=200, height=200)
        self.finish_button.place(x=0, y=250, width=100, height=30)
        self.entry.place(x=250, y=50, width=200, height=30)
        self.add_button.place(x=250, y=110, width=100, height=30)
        self.important_checkbox.place(x=250, y=80, width=100, height=30)
        self.delete_button.place(x=0, y=290, width=100, height=30)
        self.save_button.place(x=0, y=320, width=100, height=30)
        self.date_picker.place(x=250, y=150, width=200, height=200)
        self.sort_by_label.place(x=0, y=0, width=50, height=30)
        self.sort_by_name_button.place(x=50, y=0, width=50, height=30)
        self.sort_by_date_button.place(x=100, y=0, width=50, height=30)

        disk_data = database.load_from_disk()
        if disk_data is not None:
            for item in disk_data:
                self.task_list.append(item)

        # change app icon
        root.iconbitmap("icon.ico")

        # Start the Tkinter event loop
        root.mainloop()
