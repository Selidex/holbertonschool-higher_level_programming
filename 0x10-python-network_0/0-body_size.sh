#!/bin/bash
# recieves body size of a site
curl -s "$1" | wc -c
