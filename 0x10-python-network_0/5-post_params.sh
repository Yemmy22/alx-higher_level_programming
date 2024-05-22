#!/bin/bash
# This script sends key/value pair data in a post request with curl.
curl -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
