#!/usr/bin/python3
'''
A module that fetches a url and display reponse body in tabulated format
'''
import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()

        print("Body response:")
        print("\t- type:", type(page))
        print("\t- content:", page)
        print("\t- utf8 content:", page.decode('utf-8'))
