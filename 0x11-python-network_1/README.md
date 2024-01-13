# 0x11. Python - Network #1

This repository continues exploring network programming in Python with a focus on low-level sockets and client-server applications. The goal is to learn how to build networked applications from the ground up using sockets.

## Learning Objectives

- How to fetch internet resources with the Python package urllib 
- How to decode urllib body response
- How to use socket programming basics (TCP and UDP) in Python 
- How to listen for events on the socket such as client connection
- How to receive/send data from/to a socket 
- How to handle multiple client connections on the same socket
- How to work with threading in Python
- How to maximize code reuse with functions
- How to use user data to determine response

## Project Overview

The projects are split into the following tasks:

- 0-hello_bind.py - Binds socket to port 12345 and listens for connections
- 1-hello_connect.py - Connects to a server on port 12345 and prints message received
- 2-hello_server.py - Listens for connections and prints client message
- 3-hex.py - Takes in IP address and port as args, connects and prints hex representation
- 4-stock_prices.py - Displays stock prices from a server in a user-friendly format
- 5-request_header.py - Takes in URL, sends request and displays value of header
- 6-post_request.py - Takes in URL and letter, sends POST request and displays body
- 7-error_code.py - Takes in URL, sends request and displays body if 2xx, error code otherwise
- 8-my_head.py - Takes in URL, sends HEAD request and displays header values
- 9-starwars.py - Sends search request and displays number of results

## Usage

Each Python file contains documentation and can be run independently.

## Testing 

Test files will be added to validate socket functionality.
