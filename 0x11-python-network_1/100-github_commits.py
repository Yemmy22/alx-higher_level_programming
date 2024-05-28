#!/usr/bin/python3

'''
A request module that sends request for repository commits
to github api and list the most recent commits
in a specified format.
'''

import requests
from sys import argv

if __name__ == "__main__":

    url = 'https://api.github.com/repos'
    user = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/'

    request = requests.get(url + user + '/' + repo + '/commits')
    json_page = request.json()
    for log in json_page[:10]:
        print("{}: {}".format(log['sha'], log['commit']['author']['name']))

'''
Alternatively print statement could be:
print(f"{log.get('sha')}: {log.get('commit').get('author').get('name')}")
'''
