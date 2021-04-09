#!/usr/bin/python3
"""Headers again, different module"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    dic = r.headers
    print(dic.get('X-Request-Id'))
