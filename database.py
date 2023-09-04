from task_item import TaskItem
import json

file_path = 'output.json'


def task_item_to_dict(task: TaskItem):
    dict_output = {"task_title": task.task_title, "is_important": task.is_important}
    return dict_output


def save_to_disk(task_list: list):
    print("save_to_disk")
    list_of_dict = []
    for item in task_list:
        list_of_dict.append(task_item_to_dict(item))
    json_string = json.dumps(list_of_dict)
    with open(file_path, 'w') as json_file:
        json_file.write(json_string)


def load_from_disk():
    try:
        with open(file_path, 'r') as file:
            chars = file.read()

        json_string = ""

        for c in chars:
            json_string += c

        data_dict = json.loads(json_string)

        # Now 'data_dict' is a dictionary containing the JSON data
        print(data_dict)

        return data_dict
    except:
        return
