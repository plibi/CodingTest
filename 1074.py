import sys
N, r, c = map(int, sys.stdin.readline().split())

def visit(count, row, col, end_row, end_col):
    if row == r and col == c:
        return count

    mid_row = ...
    # bottom right
    if row > 2**end_row//2-1 and col > 2**end_col//2-1:
        count += 2**end_row + 1
        return visit(count,2**end_row//2-1, 2**end_col//2-1, end_row, )
    # bottom left
    if row > 2**end_row//2-1 and col <= 2**end_col//2-1:
        ...
    # top right
    if row <= 2**end_row//2-1 and col > 2**end_col//2-1:
        ...
    # top left
    if row <= 2**end_row//2-1 and col <= 2**end_col//2-1:
        ...

# 2 3 1
