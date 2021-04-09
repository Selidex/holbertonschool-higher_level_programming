#!/usr/bin/python3
"""POST an email"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        dedata = response.read()
        dedata = dedata.decode("UTF-8")
        print(dedata)
