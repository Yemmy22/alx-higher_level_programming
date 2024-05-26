#!/usr/bin/python3

'''
This module posts a email in a requets and returns it in the reponse
'''

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}

    response = requests.post(url, data)
    print(response.text)
