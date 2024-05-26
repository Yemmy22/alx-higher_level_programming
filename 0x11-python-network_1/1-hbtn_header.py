#!/usr/bin/python3

'''
A module that displays the value of a header field in a HTTP reresponse
'''

import sys
from urllib.request import urlopen

if __name__ == "__main__":

    url = sys.argv[1]

    with urlopen(url) as response:
        header = response.headers
        if 'X-Request-Id' in header:
            print(header['X-Request-Id'])
