"""
This function computes the factorial of a number - recursively
"""


def factorial(n):
    if n <= 0:
        return 1
    else:
        val = n * factorial(n-1)
        return val