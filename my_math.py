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
