#!/usr/bin/python3
"""Exports an employee's TODO list to a JSON file."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]
    with open(filename, "w") as f:
        json.dump({str(employee_id): tasks}, f)
