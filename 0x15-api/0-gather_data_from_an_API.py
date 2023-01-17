#!/usr/bin/python3
"""
Script, using REST API, that gives TODO list progress
rusing given eomplyee ID
"""
import json
import sys
import urllib.request


def todo_list_progress(employee_id):
    """Make API request"""
    url = ("https://jsonplaceholder.typicode.com/todos?userId{}"
           .format(employee_id))
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    """get to filter complete tasks"""
    TASK_TITLE = [task for task in data if task["completed"]]
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
    TOTAL_NUM_OF_TASKS = len(data)

    """Getting employee name"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = urllib.request.urlopen(url)
    employee_data = json.loads(response.read())
    EMPLOYEE_NAME = employee_data["name"]

    """printing the output in a specific format"""
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t{}['title']".format(task))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)
