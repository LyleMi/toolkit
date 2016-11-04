import hashlib
import itertools

charset = ''.join([chr(i) for i in range(128)])


def md5(s):
    return hashlib.md5(s).hexdigest()


def sha256(s):
    return hashlib.sha256(s).hexdigest()


def crack(compare):
    for k in range(1, len(charset) + 1):
        for i in itertools.permutations(charset, k):
            if compare(i):
                return ''.join(i)


def test(i):
    return md5(''.join(i)) == '03c7c0ace395d80182db07ae2c30f034'


if __name__ == '__main__':
    print crack(test)
