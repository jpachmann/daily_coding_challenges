"""Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) /
2.0)). You can assume that such element exists. For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""


def solution(list_x):
    counter = {}
    for item in list_x:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1

        if counter[item] >= len(list_x) // 2:
            return item


if __name__ == "__main__":
    print(solution([1, 2, 1, 1, 3, 4, 0]))
