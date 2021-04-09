#!/usr/bin/python3
""" This script fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(str(data)))
        dedata = data.decode('UTF-8')
        print('\t- utf8 content: {}'.format(dedata))
