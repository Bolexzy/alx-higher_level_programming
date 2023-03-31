#!/bin/bash
# Sends a GET request to the URL using curl, and displays the body of the response # A header variable X-School-User-Id must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
