#!/usr/bin/python3
"""

Python script that, using this REST API

(https://jsonplaceholder.typicode.com/), for a given employee ID, returns

information about his/her TODO list progress and to export data in the JSON

format.

"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

  t = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = t.json().get('username')

    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    data = t.json()

    output = {}
    output['{}'.format(argv[1])] = []
    for task in data:
        output['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(output, file)
