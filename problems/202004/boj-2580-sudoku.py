# 백준 2580 : 스도쿠
# https://www.acmicpc.net/problem/2580
# 시간 : 60분
# 경과 : 못 품, 솔루션(https://claude-u.tistory.com/360)보고 정리
#! 복습 필수

sudoku = [list(map(int, input().split())) for _ in range(9)]

# 0의 좌표 위치만 받고, 그 0들만 채워나가는 식으로 백트랙킹
#! 백트랙킹 문제에서는 얼마나 반복을 최소화할 수 있을지에 대해 생각해야한다
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

#! 유망 숫자들을 뽑아야 한다는 생각은 했었는데, 0을 순회하면서 한번에 뽑아야겠다고 생각을 못함
# 가능한 숫자들의 리스트를 뽑아줌


def is_promising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행과 열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    # 3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])

    return promising


flag = False  # 답이 출력되었는가?

#! 문제에서는 딱 하나만 출력되면 땡이므로 백트랙킹 중에 결과로 답이 이미 출력되었을 때는 다른 재귀호출은 이제 안해도 됨
# * 좋은 방법인듯,, 문제 조건에 따라서 적용해보면 좋을 거 같다


def dfs(x):
    global flag

    if flag:  # 이미 답이 출력된 경우
        return

    if x == len(zeros):  # 마지막 0까지 다 채웠을 경우
        for row in sudoku:
            # ? 여기 애스터리크 의미?
            print(*row)
        flag = True  # 답 출력
        return

    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)  # 유망한 숫자들을 받음

        for num in promising:
            sudoku[i][j] = num  # 유망한 숫자 중 하나를 넣어줌
            dfs(x + 1)  # 다음 0으로 넘어감
            #! 백트랙킹에서 재귀호출 후 다음 문이 실행되는건 답이 안나왔을 경우(len zero만큼 못간 경우)
            #! dfs 타고 쭉 가고 난 후 답 출력될때까지 갔으면 이 뒤는 호출 안됨
            #! 답이 없는 경우 : 유망한 숫자들이 하나도 안나올 경우에는 for문이 돌아가지 않는다 => dfs가 실행되지 않음 => 그동안 스도쿠에 써왔던 답 초기화해야함
            sudoku[i][j] = 0  # 초기화 (정답이 없을 경우를 대비)


dfs(0)

#! 못푼 이유1) 너무 엔퀸 문제처럼 생각했다,,,, 가능성을 열어두자 제발!!
# * 유연하게 풀자 유연하게... 모든 문제가 풀어봤던 문제처럼은 안 될 가능성이 높다
# * 백트랙킹 유형이란걸 확인했을 때는, 최소한의 반복으로 수를 채울 방법을 생각했어야 했다 => 0만 순회하기

#! 못푼 이유2) 손코딩 과정에서 해야할 일이 완벽하게 정리가 안 된 상태에서 자꾸 코드를 썼다
# * 손코딩을 하더라도 코드부터 쓰지말자!!!!!! 뭘 해야될지부터 정리하자 확실하게
# * 그 다음부터 손으로 코드를 짜자
