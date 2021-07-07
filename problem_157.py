"""Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should
return false, since there's no rearrangement that can form a palindrome.
"""
import math


def solution(s):
    # Palindrome if at most 1 character has no duplicate
    uneven = sum(1 for char in s if s.count(char) % 2 != 0)
    return uneven <= 1


if __name__ == "__main__":
    print(solution("carrace"))
    print(solution("daily"))
