#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from github import Github


def main():
    username = sys.argv[1]
    g = Github()
    user = g.get_user(username)
    stars = 0
    forks = 0
    repos = user.get_repos()
    for repo in repos:
        print(repo.name, repo.stargazers_count, repo.forks_count)
        stars += repo.stargazers_count
        forks += repo.forks_count

    print(stars)
    print(forks)


if __name__ == '__main__':
    main()
