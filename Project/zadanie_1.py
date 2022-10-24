#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def srgeo(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        n = len(values)
        p = 1
        for value in values:
            p *= value
            g = pow(p, 1/n)
            return g

    else:
        return None


if __name__ == "__main__":
    print(srgeo())
    print(srgeo(3.5, 2.4, 0.2, 0.3, 1000))