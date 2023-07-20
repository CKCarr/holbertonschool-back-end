#!/usr/bin/python3
""" Gather data from an API """
import urllib.request
import json
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Make a GET request to the API
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = urllib.request.urlopen(url)
        todos = json.loads(response.read())

        # Extract employee information
        employee_name = todos[0]['username']

        # Filter completed tasks
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)

        # Print the employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        print(f"{employee_name}:")

        # Print the title of completed tasks
        for task in completed_tasks:
            print(f"\t{task}")

    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")

    except urllib.error.URLError as e:
        print(f"Error: Failed to connect to the server - {e.reason}")

    except json.JSONDecodeError as e:
        print("Error: Failed to parse JSON response")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
