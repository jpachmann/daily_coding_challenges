"""Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.
Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""
import math


def solution(n):
    # Using Lagrange’s four-square theorem

    if n < 4:
        return n

    if int(math.sqrt(n)) ** 2 == n:
        return 1

    while n % 4 == 0:
        n //= 4

    if n % 8 == 7:
        return 4

    x = int(math.sqrt(n))
    for i in range(1, x + 1):
        rest = n - i * i
        if int(math.sqrt(rest)) ** 2 == rest:
            return 2

    return 3


if __name__ == "__main__":
    print(solution(13))
    print(solution(27))
