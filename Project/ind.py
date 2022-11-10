#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Сумма аргументов, расположенных между первым и вторым положительными аргументами.
"""


def sumplus(*args):
    pos1 = -1
    pos2 = -1
    if args:
        for arg in args:
            if arg > 0:
                pos1 = args.index(arg)
                break

        for arg in args[pos1 + 1:]:
            if arg > 0:
                pos2 = args.index(arg)
                break

        return sum([arg for arg in args[pos1 + 1: pos2]])

    else:
        return None


if __name__ == "__main__":
    print(sumplus())
    print(sumplus(2, -3.25, - 4, 0, -2.4, 1))