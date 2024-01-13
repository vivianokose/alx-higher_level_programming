#!/bib/bash
# A script that takes a URL and displays the allowed OPTIONS.
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
