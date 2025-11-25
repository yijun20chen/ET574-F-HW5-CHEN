# Yi Jun Chen 24696599
# my_math.py

def fibonacci(n):
    """
    Return the n-th Fibonacci number (0-indexed).
    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("fibonacci(n) requires an integer n")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def mean(values):
    """
    Return the arithmetic mean of a non-empty iterable of numbers.
    Raises:
        ValueError: if values is empty
        TypeError: if any element is not a number
    """
    total = 0.0
    count = 0

    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("mean() expects all elements to be numbers")
        total += float(v)
        count += 1

    if count == 0:
        raise ValueError("mean() of empty data")

    return total / count

def comb(n, k):
    """
    pretty silly seeing this in the description when my mouse hovers over it
    """
    if not isinstance(n, int):
        raise TypeError("comb(n, k) requires an integer n")
    if not isinstance(k, int):
        raise TypeError("comb(n, k) requires an integer k")
    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")
    if k > n:
        return 0
    
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    
    return factorial(n) // (factorial(k) * factorial(n - k))


def stdev(values, ddof=0):
    """
    Return the (population or sample) standard deviation of a non-empty iterable of numbers.

    Parameters:
        values: iterable of numbers
        ddof: delta degrees of freedom (0 for population, 1 for sample)

    Raises:
        ValueError: if values is empty or n - ddof <= 0
        TypeError: if any element is not a number
    """
    if not isinstance(values, (list, tuple)):
        raise TypeError("values must be a list or tuple")
    if not isinstance(ddof, int):
        raise TypeError("ddof must be an integer")
    n = len(values)
    if n == 0:
        raise ValueError("stdev() of empty data")
    if n - ddof <= 0:
        raise ValueError("ddof >= n results in division by zero")

    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("stdev() expects numeric values")

    mu = mean(values)
    ss = 0.0
    for v in values:
        dv = float(v) - mu
        ss += dv * dv

    variance = ss / (n - ddof)
    return variance ** 0.5

def binomial_cdf(k, n, p):
    """
    Cumulative distribution function for Binomial(n, p): P(X <= k).

    Parameters:
        k: integer threshold (0 <= k <= n)
        n: number of trials (int, >= 0)
        p: success probability (0 <= p <= 1)

    Returns:
        number between 0 and 1

    Raises:
        TypeError: if n or k is not an int
        ValueError: if n < 0, k < 0, or p not in [0, 1]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if not isinstance(k, int):
        raise TypeError("k must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")
    if k > n:
        raise ValueError("k cannot be greater than n")
    if not (0.0 <= p <= 1.0):
        raise ValueError("p must be between 0 and 1")

    # quick shortcuts for extreme p
    if p == 0.0:
        if k >= 0:
            return 1.0
        else:
            return 0.0
    if p == 1.0:
        if k >= n:
            return 1.0
        else:
            return 0.0

    cdf = 0.0
    for i in range(0, min(k, n) + 1):
        cdf += comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) # exact probability of success on nth trial (my favorite part)

    return cdf