#!/usr/bin/env python3


def first(limit):
    sz = limit // 10
    houses = [0 for i in range(sz)]

    for i in range(1, sz):
        for j in range(i, sz, i):
            houses[j] += i

    for i in range(len(houses)):
        print("%d %d" % (i, houses[i]))
        if houses[i] > limit // 10:
            return i


def second(limit):
    pass


if __name__ == '__main__':
    res = first(36_000_000)
    print(">>> %s" % res)

    # res = second(data)
    # print(">>> %s" % res)

