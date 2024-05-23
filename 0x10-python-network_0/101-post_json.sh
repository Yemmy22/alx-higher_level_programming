#!/bin/bash
# This script sends in an HTTP POST request, a data from a json file.
curl -H "Content-Type: application/json" -d @"$2" -X POST "$1"
