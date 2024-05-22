#!/bin/bash
# This script displays the size in byte of an http response.
curl -sI "$1" | grep "Content-Length" | sed 's/^Content-Length: //'
