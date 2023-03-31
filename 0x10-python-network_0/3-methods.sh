#!/bin/bash
# Script that takes in a URL and shows the Allowed OPTIONS
curl -sIX OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-
