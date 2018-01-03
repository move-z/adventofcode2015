#!/usr/bin/env python3


def first(digits):
    def apply(digits):
        curr_digit = None
        curr_num = 1
        next_num = []
        for c in digits:
            if curr_digit is not None:
                if c == curr_digit:
                    curr_num += 1
                else:
                    next_num.append(str(curr_num))
                    next_num.append(curr_digit)
                    curr_num = 1
            curr_digit = c
        next_num.append(str(curr_num))
        next_num.append(curr_digit)
        return "".join(next_num)

    for i in range(40):
        digits = apply(digits)
    return len(digits)


def second(digits):
    def apply(digits):
        curr_digit = None
        curr_num = 1
        next_num = []
        for c in digits:
            if curr_digit is not None:
                if c == curr_digit:
                    curr_num += 1
                else:
                    next_num.append(str(curr_num))
                    next_num.append(curr_digit)
                    curr_num = 1
            curr_digit = c
        next_num.append(str(curr_num))
        next_num.append(curr_digit)
        return "".join(next_num)

    for i in range(50):
        digits = apply(digits)
    return len(digits)


if __name__ == '__main__':
    res = first("3113322113")
    print(">>> %s" % res)

    res = second("3113322113")
    print(">>> %s" % res)
