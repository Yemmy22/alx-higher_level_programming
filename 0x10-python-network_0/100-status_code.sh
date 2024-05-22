#!/bin/bash
# This script returns only the status code of an HTTP reponse.
curl -o /dev/null -sw '%{response_code}' "$1"
