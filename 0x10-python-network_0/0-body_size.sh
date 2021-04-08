#!/bin/bash
# recieves body size of a site
curl -sI $"1" | grep -i Content-Length | awk '{print $2}'
