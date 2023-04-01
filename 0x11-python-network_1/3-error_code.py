#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
from urllib import parse, request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
