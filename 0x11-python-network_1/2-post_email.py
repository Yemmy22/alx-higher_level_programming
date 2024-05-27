#!/usr/bin/python3
'''
A module that posts data in a HTTP request and displays the datain response.
'''

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data)as response:
        page = response.read()
        print(page.decode('utf-8'))
