#!/bin/bash
# recieves body size of a site
curl -s "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST
