#!/usr/bin/python3
"""Script that returns information about his/her TODO list progress"""
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """Defines the Script"""
    # Construct the URL using the employee ID
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    
    # Make the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        done_tasks = sum(1 for todo in todos if todo['completed'])
        
        # Extracting employee name from the first todo item
        employee_name = todos[0]['userId']
        
        print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
        
        # Printing each completed task title
        for todo in todos:
            if todo['completed']:
                print("\t{}".format(todo['title']))
    else:
        print("Failed to retrieve data")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
