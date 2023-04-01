#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import parse, request
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(sys.argv[1], data)

    with request.urlopen(req) as res:
        html = res.read()
        print(html.decode('utf-8'))
