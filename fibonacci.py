"""
Program to generate Fibonacci number

"""


known = {0:0,1:1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


def sum_of_fibo(n):
    total = sum(known.values())
    return total




print(fibonacci(7))
print(sum_of_fibo(7))