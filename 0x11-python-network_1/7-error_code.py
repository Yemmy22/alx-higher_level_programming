#!/usr/bin/python3

'''
This module sends a request to a url and displays the body of
response if successful or the status code if it fails
'''

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
