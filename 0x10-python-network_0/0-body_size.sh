#!/bin/bash
# cript that shows the Content-Length from a HTTP response body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
