import hashlib
import itertools

charset = string.printable
charset = ''.join([chr(i) for i in range(128)])


def md5(s):
    return hashlib.md5(s).hexdigest()


def sha256(s):
    return hashlib.sha256(s).hexdigest()


def crack(func):
    def handle_args(*args, **kwargs):
        for k in range(1, len(charset) + 1):
            for i in itertools.permutations(charset, k):
                s = ''.join(i)
                if func(s):
                    print s
                    exit()
    return handle_args

@crack
def md5crack(x):
    return md5(x) == '03c7c0ace395d80182db07ae2c30f034'


if __name__ == '__main__':
    print md5crack()
