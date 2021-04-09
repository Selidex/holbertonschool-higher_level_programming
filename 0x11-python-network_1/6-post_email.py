#!/usr/bin/python3
"""Headers again, different module"""
import requests
import sys


if __name__ == "__main__":
    dic = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=dic)
    print(r.text)
