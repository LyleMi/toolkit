import os


def traverseDir(path):
    print 'init path:', path
    for i in os.listdir(path):
        if os.path.isdir(i):
            print 'dir', os.path.join(path, i)
            traverseDir(os.path.join(path, i))
        elif os.path.isfile(i):
            print 'file', i

if __name__ == '__main__':
    traverseDir(os.getcwd())
