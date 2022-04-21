#!/bin/bash
#Create a curl requests that send a Json file
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
