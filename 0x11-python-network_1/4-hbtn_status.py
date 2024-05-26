#!/usr/bin/python3

'''
A module that fetches a specified url and formats the output
'''

import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    page = response.text
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
