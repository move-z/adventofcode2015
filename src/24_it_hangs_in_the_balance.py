#!/usr/bin/env python3
import itertools
import operator
from functools import reduce


def first(*packages):
    group_weight = sum(packages) // 3

    i = 2
    while True:
        legs = itertools.combinations(packages, i)
        legs = [l for l in legs if sum(l) == group_weight]

        if not legs:
            i += 1
            continue

        return min([reduce(operator.mul, l, 1) for l in legs])


def second(*packages):
    group_weight = sum(packages) // 4

    i = 2
    while True:
        legs = itertools.combinations(packages, i)
        legs = [l for l in legs if sum(l) == group_weight]

        if not legs:
            i += 1
            continue

        return min([reduce(operator.mul, l, 1) for l in legs])


if __name__ == '__main__':
    data = (
        1,
        3,
        5,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
