#!/usr/bin/env bash
#Create a curl requests, and display the size in bytes of the response
curl -Is "$1" | grep "Content-Length" | cut -d ' ' -f2
