#!/bin/bash
# This script sends in an HTTP POST request, a data from a json file.
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
