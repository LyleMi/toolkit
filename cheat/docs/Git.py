#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Git(Base):

    _doc = {
        "config": """
// show config
git config --global -l

// LF will be replaced by CRLF
git config --global core.autocrlf false

git config core.ignorecase false

// set credential cache
git config --global credential.helper "cache --timeout=3600"
git config --global credential.helper store
// for credential on windows
git config --global credential.helper wincred

git config user.name "username"
git config user.email "email@example.com"

// close SSL CERT verification for speed up
git config --global http.sslVerify false

// proxy
git config --global https.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
git config --global https.proxy 'socks5://127.0.0.1:10808'

git config --global --unset http.proxy
git config --global --unset https.proxy

// proxy only for github
git config --global http.https://github.com.proxy socks5://127.0.0.1:1080
git config --global --unset http.https://github.com.proxy
""",
        "branch": """
// pull remote branch list
git branch -r

// pull remote branch
git checkout -b local_branch_name origin/remote_branch_name

// list all branch
git branch -av

// create new branch based current branch
git branch <new branch>

// delete local branch
git branch -d

// delete remote branch
git push origin --delete <branchName>

// synchronize branch
git checkout master
git merge dev
""",
        "pr": """
git remote add upstream https://

// synchronize after pull request
git fetch upstream
git merge upstream/master
git reset --hard upstream/master
git push -f
""",
        "log": """
git log --oneline
git log --oneline --decorate

git log -p
git log --stat
git log --graph --oneline --decorate
git log --pretty="%cn committed %h on %cd"

git log --after="2018-12-1"
git log --after="yesterday"
git log --before="yesterday"
git log --author="auother"

git log --diff-filter=D --summary
""",
        "tag": """
// list all tag
git tag
// new tag
git tag [tagname] -light
// checkout
git checkout [tagname]
// add tag for commit
git tag -a [tagname] [commit hash]
// add tag to server
git push origin [tagname]
// delete tag
git tag -d [tagname]
""",
        "big repo": """
// pull
git clone --depth 1 <repo_URI>
git fetch --unshallow
git pull --all
git pull origin master --allow-unrelated-histories

rsync .git <repo_URI>/.git

// push
git gc
""",
        "delete file": """
git filter-branch --tree-filter "rm -f path/to/file" -- --all
git push -u origin --all
"""
    }


if __name__ == '__main__':
    GitDoc.show()
