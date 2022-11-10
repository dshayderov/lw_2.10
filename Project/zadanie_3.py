#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Даны значения площади городов в виде ключ-значения.
Определить наибольшую и среднюю площадь.
"""


def scity(**kwargs):
    summa = 0
    n = len(kwargs)
    max = 0
    for kw in kwargs:
        summa += kwargs[kw]
        if kwargs[kw] > max:
            max = kwargs[kw]
    return max, summa/n


if __name__ == "__main__":
    print(scity(
        Москва=2511,
        Петербург=1439,
        Ставрополь=171,
        Краснодар=339,
        Волгоград=859,
    ))