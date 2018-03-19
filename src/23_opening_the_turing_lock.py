#!/usr/bin/env python3


def first(*instructions):
    regs = {
        'a': 0,
        'b': 0
    }

    i = 0
    while True:
        if i < 0 or i >= len(instructions):
            break

        instruction, arg = instructions[i].split(" ", maxsplit=1)

        if instruction == 'hlf':
            regs[arg] /= 2
        elif instruction == 'tpl':
            regs[arg] *= 3
        elif instruction == 'inc':
            regs[arg] += 1
        elif instruction == 'jmp':
            i += int(arg)
            continue
        elif instruction == 'jie':
            arg, arg2 = arg.split(", ")
            if regs[arg] % 2 == 0:
                i += int(arg2)
                continue
        elif instruction == 'jio':
            arg, arg2 = arg.split(", ")
            if regs[arg] == 1:
                i += int(arg2)
                continue

        i += 1

    return regs['b']


def second(*instructions):
    regs = {
        'a': 1,
        'b': 0
    }

    i = 0
    while True:
        if i < 0 or i >= len(instructions):
            break

        instruction, arg = instructions[i].split(" ", maxsplit=1)

        if instruction == 'hlf':
            regs[arg] /= 2
        elif instruction == 'tpl':
            regs[arg] *= 3
        elif instruction == 'inc':
            regs[arg] += 1
        elif instruction == 'jmp':
            i += int(arg)
            continue
        elif instruction == 'jie':
            arg, arg2 = arg.split(", ")
            if regs[arg] % 2 == 0:
                i += int(arg2)
                continue
        elif instruction == 'jio':
            arg, arg2 = arg.split(", ")
            if regs[arg] == 1:
                i += int(arg2)
                continue

        i += 1

    return regs['b']


if __name__ == '__main__':
    data = (
        'jio a, +22',
        'inc a',
        'tpl a',
        'tpl a',
        'tpl a',
        'inc a',
        'tpl a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'jmp +19',
        'tpl a',
        'tpl a',
        'tpl a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'inc a',
        'tpl a',
        'inc a',
        'tpl a',
        'tpl a',
        'jio a, +8',
        'inc b',
        'jie a, +4',
        'tpl a',
        'inc a',
        'jmp +2',
        'hlf a',
        'jmp -7'
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
