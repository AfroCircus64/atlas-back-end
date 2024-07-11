#!/usr/bin/python3
"""Script that returns information about his/her TODO list progress"""
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """Defines the Script"""
    # Construct the URL using the employee ID
    base_url = "https://jsonplaceholder.typicode.com"
    url = "{}/todos?userId={}".format(base_url, employee_id)
    employee_url = "{}/users/z{}".format(base_url, employee_id)

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        done_tasks = sum(1 for todo in todos if todo['completed'])

        # Extracting employee name
        employee_data = requests.get(employee_url).json()
        employee_name = employee_data.get('name')

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks, total_tasks))

        todos_response = requests.get(
            "{}/todos".format(base_url), params={'userId': employee_id}
        )
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get('completed')]
        number_of_done_tasks = len(done_tasks)

        print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name, number_of_done_tasks, total_tasks)
        )
        for task in done_tasks:
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
