#!/usr/bin/python3

'''
A module that returns a fetched page or the error code of failed http request
'''

from sys import argv
from urllib.request import urlopen, Request
from urllib.error import URLError

url = argv[1]
req = Request(url)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'code'):
        print("Error code:",  e.code)
else:
    fetch = response.read()
    print(fetch.decode('utf-8'))
