#!/bin/bash
# This script sends a POST request and shows the body of the response.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
