#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o /dev/null -w "%{http_code}\n" $1 | grep 200 && curl -sX GET $1