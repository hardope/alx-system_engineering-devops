#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    uid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + uid
    res = requests.get(url)
    USERNAME = res.json().get('username')
    url_to_task = url + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    with open('{}.csv'.format(uid), 'w') as csvfile:
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            """print(TASK_COMPLETED_STATUS)"""
            TASK_TITLE = task.get('title')
            """print(TASK_TITLE)"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                uid, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE))
