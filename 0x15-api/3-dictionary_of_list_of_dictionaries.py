#!/usr/bin/python3
"""
Python script that, using this REST API
(https://jsonplaceholder.typicode.com/), records all tasks from all
employees, returns information about his/her TODO list progress and to
export data in the JSON format.
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    ids = set()
    t = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = t.json()

    for user in data:
        ids.add(user.get('userId'))

    output = {}
    for user in ids:
        t = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(user))
        username = t.json().get('username')

        t = requests.get('https://jsonplaceholder.typicode.com/' +
                         'todos?userId={}'.format(user))
        data = t.json()

        output['{}'.format(user)] = []
        for task in data:
            output['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump({int(x): output[x] for x in output.keys()},
                  file, sort_keys=True)
