#!/usr/bin/env python3
from hashlib import md5
import sys


def first(key):
    for i in range(sys.maxsize):
        h = md5()
        h.update((key + str(i)).encode('ascii'))
        if h.hexdigest()[:5] == '00000':
            return i


def second(key):
    for i in range(sys.maxsize):
        h = md5()
        h.update((key + str(i)).encode('ascii'))
        if h.hexdigest()[:6] == '000000':
            return i


if __name__ == '__main__':
    res = first('ckczppom')
    print(">>> %d" % res)

    res = second('ckczppom')
    print(">>> %d" % res)
