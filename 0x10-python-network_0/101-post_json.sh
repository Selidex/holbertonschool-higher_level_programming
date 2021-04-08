#!/bin/bash
# recieves body size of a site
curl "$1" -s -H "Content-Type: application/json" -d "$2"
