#!/usr/bin/python
""" returns information about his/her TODO list progress """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [tmp.get("title") for tmp in todos if tmp.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
