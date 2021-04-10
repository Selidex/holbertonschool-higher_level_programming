#!/usr/bin/python3
"""Headers again, different module"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    query_url = "https://api.github.com/users/{}".format(user)
    params = {"state": "open", }
    headers = {'Authorization': 'token {}'.format(token)}
    r = requests.get(query_url, headers=headers, params=params)
    rj = r.json()
    print(rj.get('id'))
