#!/usr/bin/python3
"""
A Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], username, t.get("completed"), t.get("title")]
        ) for t in todos]
