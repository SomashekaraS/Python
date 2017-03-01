"""
This function computes and returns a list of all the factors of a number n
"""

from even_odd import divides


def factors(n):
    flist = list()
    for i in range(1, n + 1):
        if divides(i, n):
            flist.append(i)
    return flist

