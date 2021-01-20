#!/usr/bin/python3
"""This module appends data to a json file"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """main function that does the things"""
    filename = "add_item.json"
    try:
        finit = load_from_json_file(filename)
    except:
        finit = []
    finit += sys.argv[1:]
    save_to_json_file(finit, filename)


if __name__ == "__main__":
    main()
