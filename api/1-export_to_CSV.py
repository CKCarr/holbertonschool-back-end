#!/usr/bin/python3
"""Script that prints specific information from an API"""
import requests
import sys
import csv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    id = sys.argv[1]
    request = requests.get('{}/users/{}/todos'.format(
        API_URL, id), params={"_expand": "user"})

    response = request.json()

    completed_tasks = [task for task in response if task['completed']]
    EMPLOYEE_NAME = response[0]['user']['name']
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(response)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))

    for task in completed_tasks:
        print("\t {}".format(task['title']))

    # Export to CSV
    filename = "{}.csv".format(id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in response:
            writer.writerow(
                [id, EMPLOYEE_NAME, str(task['completed']), task['title']])

    print("Data exported to {} successfully!".format(filename))

