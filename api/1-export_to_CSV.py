#!/usr/bin/python3
"""Script that prints specific information from an API"""
import csv
import requests
import sys


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
        print("\t {}".format(task['title']
                             ))

    # Export to CSV
    csv_filename = "{}.csv".format(id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

        for task in response:
            task_completed_status = "True" if task['completed'] else "False"
            writer.writerow(
                [id, EMPLOYEE_NAME, task_completed_status, task['title']])

    print("Data exported to {}".format(csv_filename))
