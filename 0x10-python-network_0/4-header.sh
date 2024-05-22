#!/bin/bash
# This script includes a new header in the HTTP request and displays the body of the response.
curl -H "X-School-User-Id: 98" "$1"
