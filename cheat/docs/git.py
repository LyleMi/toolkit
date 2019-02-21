#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDoc


class GitDoc(BaseDoc):

    _doc = {
        "config": """// LF will be replaced by CRLF
git config --global core.autocrlf false

// set credential cache
git config --global credential.helper "cache --timeout=3600" """,
        "branch": """// pull remote branch list
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
git merge dev""",
        "pr": """git remote add upstream https://

// synchronize after pull request
git fetch upstream
git merge upstream/master
git reset --hard upstream/master
git push -f""",
        "log": """git log --oneline
git log --oneline --decorate
git log -p
git log --stat
git log --graph --oneline --decorate
git log --pretty="%cn committed %h on %cd"
git log --after="2018-12-1"
git log --after="yesterday"
git log --before="yesterday"
git log --author="auother" """,
        "tag": """// list all tag
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
git tag -d [tagname]""",
        "pull big repo": """git clone --depth 1 <repo_URI>
git fetch --unshallow
git pull --all""",
    }


if __name__ == '__main__':
    GitDoc.show()
