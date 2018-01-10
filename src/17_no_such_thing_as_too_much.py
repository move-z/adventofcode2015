#!/usr/bin/env python3
from collections import Counter
from itertools import chain, combinations


def first(*containers):
    limit = 150

    combs = chain.from_iterable(combinations(containers, r) for r in range(1, len(containers) + 1))
    return len([comb for comb in combs if sum(comb) == limit])


def second(*containers):
    limit = 150

    combs = chain.from_iterable(combinations(containers, r) for r in range(1, len(containers) + 1))
    combs = [comb for comb in combs if sum(comb) == limit]

    sizes = Counter(len(c) for c in combs)
    return sizes[min(sizes)]


if __name__ == '__main__':
    res = first(33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42)
    print(">>> %s" % res)

    res = second(33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42)
    print(">>> %s" % res)
