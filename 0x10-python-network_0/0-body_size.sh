#!/bin/bash
# Create a curl requests, and display the size in bytes of the response
curl -sI "$1" | grep 'Content-Length:' | cut -d ' ' -f2
