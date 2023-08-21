from task_item import TaskItem
import json

file_path = 'output.json'

def task_item_to_dict(task: TaskItem):
    dict_output = {}
    dict_output["task_title"] = task.task_title
    dict_output["is_important"] = task.is_important
    return dict_output

def save_to_disk(task_list:list):
    print("save_to_disk")
    list_of_dict = []
    for item in task_list:
        list_of_dict.append(task_item_to_dict(item))
    json_string = json.dumps(list_of_dict)
    with open(file_path, 'w') as json_file:
        json_file.write(json_string)
