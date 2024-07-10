#!/bin/bash
# This script diaplays the HTTP method allowed.
curl -isX "OPTIONS" "$1" | grep "Allow" | sed 's/Allow: //'
