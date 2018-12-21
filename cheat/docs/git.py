#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseDoc

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
git push -f
""",
    }

if __name__ == '__main__':
    GitDoc.show()
