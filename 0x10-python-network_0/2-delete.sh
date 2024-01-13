#!/bin/bash
# This script sends a DELETE request to $ URL provided and display the body of the response.
curl -s "$1" -X DELETE
