# 0x10. Python - Network #0

This repository contains Python projects that explore network programming and common network tasks. The goal is to learn how to build client-server applications, handle network requests and responses, and work with low-level socket programming.

## Learning Objectives

- How to fetch internet resources with the Python package urllib
- How to decode urllib body response 
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request 
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service
- How to handle user cookies
- How to chain requests
- How to access the HTTP headers
- How to handle HTTP errors gracefully

## Project Overview

The projects are split into the following tasks:

- 0-body_size.py - Fetches a URL and prints its body size
- 1-hbtn_status.py - Fetches https://intranet.hbtn.io/status and displays the body of the response
- 2-post_email.py - Takes in a URL and email, sends a POST request, and displays the response
- 3-error_code.py - Takes in a URL, sends a request, and displays the body of the response (if 2xx code) or error message
- 4-hbtn_header.py - Displays the X-Request-Id value of a request to a URL
- 5-hbtn_headers.py - Displays all headers for a URL response
- 6-post_json.py - Takes in a URL and JSON data, sends a POST request and displays the body of the response
- 7-error_code.py - Takes in a URL, sends a request, and displays status code if not 2xx
- 8-json_api.py - Takes in a letter and sends a POST request to a URL to search users

## Usage

Each Python file can be run independently to test the network functionality.
