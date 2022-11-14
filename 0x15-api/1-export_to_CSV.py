#!/usr/bin/python3
"""
Python script that, using this REST API
(https://jsonplaceholder.typicode.com/), for a given employee ID, returns
information about his/her TODO list progress and export data in the CSV format.
"""

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    t = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = t.json().get('username')

    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    dat = t.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for task in dat:
            csv_writer.writerow([argv[1], username, task.get('completed'),
                                 task.get('title')])
