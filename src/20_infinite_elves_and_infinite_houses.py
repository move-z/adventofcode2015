#!/usr/bin/env python3


def first(limit):
    def calc(arr_sz):
        houses = [0 for i in range(arr_sz)]

        for i in range(1, arr_sz):
            for j in range(i, arr_sz, i):
                houses[j] += i

        for i in range(len(houses)):
            if houses[i] > limit // 10:
                return i

    for arr_sz in reversed(range(1, 100, 10)):
        x = calc(limit // arr_sz)
        if x is not None:
            return x


def second(limit):
    def calc(arr_sz):
        houses = [0 for i in range(arr_sz)]

        for i in range(1, arr_sz):
            for j in range(i, min(arr_sz, i * 51), i):
                houses[j] += i * 11

        for i in range(len(houses)):
            if houses[i] > limit:
                return i

    for arr_sz in reversed(range(1, 100, 10)):
        x = calc(limit // arr_sz)
        if x is not None:
            return x


if __name__ == '__main__':
    res = first(36_000_000)
    print(">>> %s" % res)

    res = second(36_000_000)
    print(">>> %s" % res)
