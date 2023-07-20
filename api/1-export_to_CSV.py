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
        print("\t {}".format(task['title']))

    # Export to CSV
    fileName = f"{EMPLOYEE_ID}.csv"

    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerow(
                [EMPLOYEE_ID, EMPLOYEE_NAME, str(task["completed"]),
                 task["title"]]
            )
