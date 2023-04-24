#!/usr/bin/python3
""" Export api to csv"""
import csv
import sys
import requests



if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """print(res.text)"""
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """print(completed)"""
            TASK_TITLE = task.get('title')
            """print(TASK_TITLE)"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, TASK_TITLE))
