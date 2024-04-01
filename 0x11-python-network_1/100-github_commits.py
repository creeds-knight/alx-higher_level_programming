#!/usr/bin/python3
""" Interview """
import sys
import requests


def interview(repo_name, ownername):
    """ Uses the git hub api to return the commits """
    url = f"https://api.github.com/repos/{ownername}/{repo_name}/commits"

    try:
        response = requests.get(url, params={'per_page': 10})
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name= commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: <repo_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    interview(repo_name, owner_name)
