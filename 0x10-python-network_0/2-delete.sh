#!/bin/bash
# This script sends a DELETE request to the URL provided as the first argument and shows the body of the response.
curl -s "$1" -X DELETE
