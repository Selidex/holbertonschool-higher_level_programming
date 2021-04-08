#!/bin/bash
# recieves body size of a site
curl "$1" -s -w "%{http_code}"
