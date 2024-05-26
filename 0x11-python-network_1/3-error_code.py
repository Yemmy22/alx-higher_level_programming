#!/usr/bin/python3

'''
A module that returns a fetched page or the error code of failed http request
'''

from sys import argv
from urllib.request import urlopen, Request
from urllib.error import URLError

if __name__ == "__main__":

    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            fetch = response.read()

    except URLError as e:
        if hasattr(e, 'code'):
            print("Error code:",  e.code)
    else:
        print(fetch.decode('utf-8'))
