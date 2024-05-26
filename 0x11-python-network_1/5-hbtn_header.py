#!/usr/bin/python3

'''
This module sends a request to the URL and displays
the value of the variable in the reponse header
'''

from sys import argv
import requests

if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
