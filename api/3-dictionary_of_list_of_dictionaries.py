#!/usr/bin/python3
"""Exports the TODO lists of all employees to a JSON file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    data = {}
    for user in users:
        uid = user.get("id")
        username = user.get("username")
        data[str(uid)] = [{"username": username,
                           "task": task.get("title"),
                           "completed": task.get("completed")}
                          for task in todos if task.get("userId") == uid]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
