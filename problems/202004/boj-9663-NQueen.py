# 백준 9663 : N Queen
# https://www.acmicpc.net/problem/9663
# 정해로 풀 때 파이썬으로는 힘들다는 의견;; : https://www.acmicpc.net/board/view/25761
# 시간 : 60분
# 경과 : 시간초과 => 시간초과(패캠 강의 참조)


N = int(input())
result = 0


def queen_valid(table, pos):
    # 현재 행 몇번째인지 구하기 (퀸의 열과 행을 모두 뽑아냈음)
    current_row = len(table)
    for queen_row in range(current_row):
        # 지금까지 나온 결과값에서의 퀸의 위치를 순회
        # 수직 체크 : 그 퀸의 위치의 col이 지금 타진할 퀸의 위치 후보의 col과 같은지
        # * 대각선 체크 : 퀸 위치의 col값에서 퀸 가능성 col값 뺀 값이
        # * 새 퀸이 들어갈 row에서 퀸이 있는 row의 값을 뺀 값과 같을 때 대각선에 위치한다
        if table[queen_row] == pos or abs(table[queen_row]-pos) == current_row - queen_row:
            return False
    return True


def DFS(num, table_result, row):
    global result
    if row == num:
        result += 1
    else:
        for col in range(num):
            if queen_valid(table_result, col):
                DFS(num, table_result + [col], row+1)


DFS(N, [], 0)
print(result)

# * dfs로직은 이제 잘 구하는데, 대각선 로직을 생각해내는데 시간이 오래걸림
