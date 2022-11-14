#!/usr/bin/python3
"""
Python script that, using this REST API
(https://jsonplaceholder.typicode.com/), for a given employee ID, returns
information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    t = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    name = t.json().get('name')

    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))

    data = t.json()
    don = tot = 0
    for task in data:
        tot += 1
        if task.get('completed'):
            don += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, don, tot))
    for task in data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
