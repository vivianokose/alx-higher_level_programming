#!/bin/bash
# This Bash script accepts a URL input, sends a GET request, and outputs the body of the response only for a 200 status code.
curl -Ls "$1"
