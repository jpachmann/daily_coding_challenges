"""Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def solution(i):
    return '{:0b}'.format(i)[::-1]


if __name__ == "__main__":
    print(solution(0b11110000111100001111000011110000))
