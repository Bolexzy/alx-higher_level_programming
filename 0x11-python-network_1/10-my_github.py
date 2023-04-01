#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
