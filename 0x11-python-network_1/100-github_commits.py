#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
