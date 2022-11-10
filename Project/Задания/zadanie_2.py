#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def srhar(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        n = len(values)
        s = 0
        for value in values:
            s += 1/value
        h = n / s
        return h

    else:
        return None


if __name__ == "__main__":
    print(srhar())
    print(srhar(5, 1, 3, 2))