def is_sudoku(puzzle):
    check = set(range(1, 10))
    for i in puzzle:          
        if set(i) != check:
            return 'INCORRECT'
    for i in range(len(puzzle)):    
        col = [j[i] for j in puzzle]
        if set(col) != check:
            return 'INCORRECT'
    for i in range(0, len(puzzle), 3):
        a = puzzle[i][:3] + puzzle[i+1][:3] + puzzle[i+2][:3]
        b = puzzle[i][3:6] + puzzle[i+1][3:6] + puzzle[i+2][3:6]
        c = puzzle[i][6:] + puzzle[i+1][6:] + puzzle[i+2][6:]
        if set(a) != check or set(b) != check or set(c) != check:
            return 'INCORRECT'
    return 'CORRECT'
          
N, *puzzles = open(0)

for i in range(int(N)):
    puzzle = []
    for j in range(10*i, 10*i+9):
        puzzle.append(list(map(int, puzzles[j].strip().split())))
    print(f'Case {i+1}:', is_sudoku(puzzle))


# =============== 수정한 버전 ================

# 정답인 스도쿠인지 판단하는 함수를 만듦
def is_sudoku(puzzle):

    # 모든 row가 만족하는지 확인
    for row in puzzle:
        if len(set(row)) < 9:
            return 'INCORRECT'

    # 모든 col이 만족하는지 확인
    for col in zip(*puzzle):
        if len(set(col)) < 9:
            return 'INCORRECT'

    # 3*3마다 만족하는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = puzzle[i][j:j+3] + puzzle[i+1][j:j+3] + puzzle[i+2][j:j+3]
            if len(set(square)) < 9:
                return 'INCORRECT'
    return 'CORRECT'


# 입력
N = int(input())
for i in range(N):
    if i > 0:
        empty = input()
    puzzle = [input().split() for _ in range(9)]

    # 정답출력
    print(f'Case {i + 1}:', is_sudoku(puzzle))