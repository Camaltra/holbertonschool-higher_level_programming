#!/usr/bin/env bash
#Create a curl post request with argument
curl -sX "POST" --data 'email=test@gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
