#!/usr/bin/env python3


def get_index(row, column):
    index = sum(range(1, column + 1))
    index += (sum(range(column, column + row - 1)))
    return index


def first(row, column):
    num = 20151125
    for i in range(1, get_index(row, column)):
        num = (num * 252533) % 33554393
    return num


if __name__ == '__main__':
    res = first(2947, 3029)
    print(">>> %s" % res)
