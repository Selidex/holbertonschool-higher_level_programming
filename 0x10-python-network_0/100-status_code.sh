#!/bin/bash
# recieves body size of a site
curl "$1" -sL -w "%{http_code}" -o /dev/null
