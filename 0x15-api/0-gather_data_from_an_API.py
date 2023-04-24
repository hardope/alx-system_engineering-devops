#!/usr/bin/python3
""" Python script to get data from an API"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url_to_api = 'https://jsonplaceholder.typicode.com/users'
    url = url_to_api + '/' + employee_id
    req = requests.get(url)
    employee_name = req.json().get('name')
    """print(employee_name)"""

    to_do_url = url + '/todos'
    req1 = requests.get(to_do_url)
    tasks = req1.json()
    """print(tasks)"""
    count_tasks = 0
    tasks_complete = []
    tasks_not_complete = []
    for task in tasks:
        if task.get('completed') is True:
            """print(task)"""
            tasks_complete.append(task)
            count_tasks += 1
            """print(count_tasks)"""
    """print(len(tasks))"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, count_tasks, len(tasks)))

    for task in tasks_complete:
        print('\t {}'.format(task.get('title')))