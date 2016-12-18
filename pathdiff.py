import os
from hashlib import sha256


def sha2(s):
    return sha256(str(s)).hexdigest()


def filesha(path):
    tmp = open(path, 'r')
    s = sha2(tmp.read())
    tmp.close()
    return s


def traverseDir(path):
    print 'init path:', path
    for i in os.listdir(path):
        if os.path.isdir(i):
            print 'dir', os.path.join(path, i)
            traverseDir(os.path.join(path, i))
        elif os.path.isfile(i):
            print 'file', i, "sha", filesha(i)

if __name__ == '__main__':
    traverseDir(os.getcwd())
