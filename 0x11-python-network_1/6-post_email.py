#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url, mail = sys.argv[1], sys.argv[2]
    value = {'email': mail}

    req = requests.post(url, data=value)
    print(req.text)
