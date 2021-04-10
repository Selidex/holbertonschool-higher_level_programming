#!/usr/bin/python3
"""Headers again, different module"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    query_url = ("https://api.github.com/repos/{}/{}/commits".
                 format(owner, repo))
    params = {"per_page": 10, }
    r = requests.get(query_url, params=params)
    rj = r.json()
    for commit in rj:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
