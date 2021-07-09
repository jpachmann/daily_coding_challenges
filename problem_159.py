"""Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def solution(s):
    for i in range(len(s)):
        if i+1 < len(s):
            if s[i] == s[i+1]:
                return s[i]


if __name__ == "__main__":
    print(solution("acbbac"))
    print(solution("abcdef"))
