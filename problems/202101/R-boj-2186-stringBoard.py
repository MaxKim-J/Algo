'''
백준 2186번 <문자판>

어렵다 진짜 그리고 사실상 DP문제였음

1. N과 M 테스트 케이스가 필요했다
2. 스켈레톤 구현한 부분마다 확실한 검증이 필요하다
3. 일단 너무 예쁘게 구현하려고 생각하지 않아야 할거같음
4. 아무리 생각해도 삼차원 배열은 에바다... enable_node를 제하더라도 문자열로 바꿔서 풀자
5. BFS로는 시간초과 DP로는 풀림
'''

N, M, K = map(int, input().split())
board = ''
for _ in range(M):
    board += input()
target = input()


def enable_node(index):
    result = []
    X = index // N
    Y = index % N

    for i in range(K):
        north, south, west, east = X-(i+1), X+(i+1), Y-(i+1), Y+(i+1)
        if -1 < west < N:
            result.append(X * N + west)
        if -1 < east < N:
            result.append(X * N + east)
        if -1 < north < M:
            result.append(north * N + Y)
        if -1 < south < M:
            result.append(south * N + Y)
    return result

# 약간의 DP랑 DFS랑 스까놓은 이상한 DFS다
# 사실 트리를 깊이우선으로 방문하긴 하지만 사실상 DP를 하기위한 것 뿐임
#! visit을 DP TABLE 처럼 사용하는 미친 내공을 보여줌


def DFS(current, idx):
    if idx == len(target):
        return 1
    if visited[current][idx] != -1:
        return visited[current][idx]
    visited[current][idx] = 0

    for next in enable_node(current):
        if board[next] == target[idx]:
            visited[current][idx] += DFS(next, idx+1)
    return visited[current][idx]


# 시작점이 되는 후보 설정
start = [i for i, elem in enumerate(board) if elem == target[0]]
visited = [[-1] * len(target) for _ in range(M*N+1)]
result = 0
for num in start:
    result += DFS(num, 1)

print(result)

'''
다른사람풀이

from collections import deque
import sys, copy
from itertools import permutations

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def dfs(y, x, idx):
    if idx == len(word):
        return 1
    if c[y][x][idx] != -1:
        return c[y][x][idx]

    c[y][x][idx] = 0
    for i in range(4):
        temp_y, temp_x = y, x
        for _ in range(k):
            ny = temp_y + dy[i]
            nx = temp_x + dx[i]
            if 0<= ny< n and 0<=nx < m:
                if a[ny][nx] == word[idx]:
                    c[y][x][idx] += dfs(ny, nx, idx+1)
            temp_y, temp_x = ny, nx
    return c[y][x][idx]


n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().strip()))
word = list(input().strip())

start = []
# dfs 후보들을 고른다
for i in range(n):
    for j in range(m):
        if a[i][j]==word[0]:
            start.append([i,j])

ans = 0
c = [[[-1]*len(word) for _ in range(m)] for _ in range(n)]
for i in range(len(start)):
    y, x = start[i]
    ans += dfs(y, x, 1)
print(ans)
'''
