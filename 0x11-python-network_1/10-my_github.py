#!/usr/bin/python3

'''
A module that makes a request to authenticate github user
with a password through the github api and return the user id
'''
from sys import argv
import requests

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    handler = requests.get(url, auth=(username, password))
    json_data = handler.json()
    print(json_data.get('id'))
