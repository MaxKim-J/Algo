sudoku = [list(map(int, input().split())) for _ in range(9)]

# 0의 위치만 확보하기 => 이친구들이 진입점이 됨
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

# 0의 행과 열의 정보를 통해 가능한 값의 전부를 리턴한다


def get_enable_nums(i, j):
    enables = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 1. 해당 숫자가 포함된 가로 세로 검사
    for k in range(9):
        if sudoku[i][k] in enables:
            enables.remove(sudoku[i][k])
        if sudoku[k][j] in enables:
            enables.remove(sudoku[k][j])

    # 2. 해당 숫자가 포함된 3*3 박스 검사

    # 큰 사각형 기준으로 3으로 나누면 전체 9개의 3*3 사각형중 어디인지 위치가 나옴
    i //= 3
    j //= 3

    # 0-3, 3-6, 6-9
    for p in range(i*3, (i+1)*3):
        # 여기도 0-3, 3-6, 6-9
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in enables:
                enables.remove(sudoku[p][q])

    return enables


# 얘는 DFS가 좋은게 일단 0들을 다 빨리 채우고 봐야됨.
# 큐에 9*9배열 넣는거 메모리에 넘 부담임


def dfs(x):
    # 마지막 0까지 다 채웠을 경우
    if x == len(zeros):
        return sudoku

    # 숫자를 채워야할 0의 위치, 그리고 가능한 숫자 배열
    (i, j) = zeros[x]
    enables = get_enable_nums(i, j)

    # 만약에 가능한 숫자가 없으면 망한 스도쿠
    if len(enables) == 0:
        return

    for num in enables:
        sudoku[i][j] = num  # 가능 숫자 중 하나를 넣어줌
        dfs(x + 1)  # 다음 0으로 넘어감
        sudoku[i][j] = 0  # 초기화


for row in dfs(0):
    print(*row)
