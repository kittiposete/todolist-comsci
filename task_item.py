class TaskItem:
    def __init__(self, task_title, is_important, date: int):
        self.task_title = task_title
        self.is_important = is_important
        self.date = date