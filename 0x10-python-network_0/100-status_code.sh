#!/bin/bash
# recieves body size of a site
curl "$1" -s -L -w "%{http_code}"
