#!/bin/bash
# recieves body size of a site
curl -s -X OPTIONS "$1" -i | grep -i "Allow: " | awk '{$1=""; print $0}'
