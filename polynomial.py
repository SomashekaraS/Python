"""
This program solves the below task.
-----
Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x^4 - 17x^2 - 3x + 5.
Each term of the polynomial can be represented as a pair of integers (coefficient,exponent).  The polynomial itself is
then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

-- Terms are sorted in descending order of exponent
-- No term has a zero cofficient
-- No two terms have the same exponent
-- Exponents are always nonnegative

For example, the polynomial introduced earlier is represented as

   [(3,4),(-17,2),(-3,1),(5,0)]

The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:

  addpoly(p1,p2)
 multpoly(p1,p2)

that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above.  Correspondingly, the outputs
 from these functions should also obey the same constraints.

"""

import collections
import itertools


def counter_to_poly(c):
    p = [(coeff, exp) for exp, coeff in c.items() if coeff != 0]
    # sort by exponents in descending order
    p.sort(key = lambda pair: pair[1], reverse = True)
    return p


def addpoly(p, q):
    r = collections.Counter()

    for coeff, exp in (p + q):
        r[exp] += coeff

    return counter_to_poly(r)


def multpoly(p, q):
    r = collections.Counter()

    for (c1, e1), (c2, e2) in itertools.product(p, q):
        r[e1 + e2] += c1 * c2

    return counter_to_poly(r)

print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))