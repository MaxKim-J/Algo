# a의 자료구조가 가장 중요했음

import sys

def move():
    # 이차원배열로 순회
    for i in range(n):
        num = i # 원래의 목적지
        for j in range(h):
            if a[num][j]: # 
                num += 1
            elif a[num-1][j]:
                num -= 1
        if i != num:
            return 0
    return 1


def dfs(cnt, idx, r):
    global ans
    # 마지막에 맞는지 확인하기
    if cnt == r:
        if move():
            ans = cnt
        return

    # 열
    for i in range(idx, h):
        # 행
        for j in range(n-1):
            # 이미 선이 있는 경우
            if a[j][i]:
                continue
            # 왼쪽에 이미 선이 있어 연속한 선을 그어버릴 수 있는 경우
            if j - 1 >= 0 and a[j-1][i]:
                continue
            # 오른쪽에 이미 선이 있어 연속한 선을 그어버릴 수 있는 경우
            if j + 1 < n and a[j+1][i]:
                continue
            # DFS로 처리
            a[j][i] = 1
            dfs(cnt + 1, i, r)
            a[j][i] = 0

n, m, h = map(int, input().split())
#! 연결관계를 저장하는 리스트 a
a = [[0]*h for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    #! x-1가로선에서 y-1에서 y로 갈 수 있음
    a[y-1][x-1] = 1

ans, flag = sys.maxsize, 1
for r in range(4):
    dfs(0, 0, r)
    if ans != sys.maxsize:
        print(ans)
        flag = 0
        break
if flag:
    print(-1)