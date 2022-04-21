#!/usr/bin/env bash
#Create a curl requests, and display the size in bytes of the response
curl -s "$1" | wc -c
