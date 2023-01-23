def find_factors(num):
    """Find factors of num.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    from functools import reduce
    factor = list(reduce(list.__add__, 
                ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))
    return factor