"""You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the
bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:
Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""


def solution(matrix, x=0, y=0):
    count = 0
    max_x, max_y = len(matrix[0]) - 1, len(matrix) - 1

    if x == max_x and y == max_y:  # found a way
        return 1

    if x < max_x and matrix[y][x + 1] == 0:
        count += solution(matrix, x + 1, y)  # look right

    if y < max_y and matrix[y + 1][x] == 0:
        count += solution(matrix, x, y + 1)  # look down

    return count


if __name__ == "__main__":
    print(solution([[0, 0, 1], [0, 0, 1], [1, 0, 0]]))
