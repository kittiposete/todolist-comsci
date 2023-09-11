class TaskItem:
    def __init__(self, task_title, is_important, date: int, is_finished=False):
        self.task_title = task_title
        self.is_important = is_important
        self.date = date
        self.is_finished = is_finished
