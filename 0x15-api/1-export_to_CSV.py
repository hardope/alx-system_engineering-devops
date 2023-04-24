#!/usr/bin/python3
""" Python script that exports an API data into csv"""
import csv
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """print(res.text)"""
    USERNAME = res.json().get('username')
    """print(USERNAME)"""
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()
    """print(tasks)
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        print(TASK_COMPLETED_STATUS)
        TASK_TITLE = task.get('title')
        print(TASK_TITLE)
    """

    with open('{}.csv'.format(USER_ID), 'w') as csvfile:
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            """print(TASK_COMPLETED_STATUS)"""
            TASK_TITLE = task.get('title')
            """print(TASK_TITLE)"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(