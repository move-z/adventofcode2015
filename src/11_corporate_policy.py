#!/usr/bin/env python3


def first(password):
    def valid(p):
        pairs = 0
        series = False
        last_c = 0
        second_last_c = 0
        for c in p:
            if not series and ord(c) == last_c + 1 and last_c == second_last_c + 1:
                series = True

            if ord(c) == last_c and ord(c) != second_last_c:
                pairs += 1

            if c in "iol":
                return False

            second_last_c = last_c
            last_c = ord(c)

        return series and pairs > 1

    def increment(p):
        p, last = p[:-1], ord(p[-1])
        last += 1
        if last > ord('z'):
            return increment(p) + 'a'
        return p + chr(last)

    while True:
        password = increment(password)
        if valid(password):
            return password


def second(password):
    return first(first(password))


if __name__ == '__main__':
    res = first("vzbxkghb")
    print(">>> %s" % res)

    res = second("vzbxkghb")
    print(">>> %s" % res)
