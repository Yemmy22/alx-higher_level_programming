#!/usr/bin/python3

'''
A module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''

from sys import argv
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError as e:
        print("Not a valid JSON")
