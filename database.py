from task_item import TaskItem
import json

file_path = 'output.json'


def task_item_to_dict(task: TaskItem):
    dict_output = {"task_title": task.task_title, "is_important": task.is_important,
                   "date": task.date, "is_finished": task.is_finished}
    return dict_output


def save_to_disk(task_list: list):
    print("save_to_disk")
    list_of_dict = []
    for item in task_list:
        list_of_dict.append(task_item_to_dict(item))
    json_string = json.dumps(list_of_dict)
    with open(file_path, 'w') as json_file:
        json_file.write(json_string)


def load_from_disk() -> list:
    try:
        with open(file_path, 'r') as file:
            chars = file.read()

        json_string = ""

        for c in chars:
            json_string += c

        data_dict = json.loads(json_string)

        task_list = []

        for item in data_dict:
            task_item = TaskItem(item["task_title"], item["is_important"], item["date"], item["is_finished"])
            task_list.append(task_item)

        return task_list
    except:
        return []
