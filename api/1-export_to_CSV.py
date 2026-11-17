#!/usr/bin/python3
"""Exports an employee's TODO list to a csv file."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    username = user.get("username")
    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])

