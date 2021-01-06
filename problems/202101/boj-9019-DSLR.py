import sys
from collections import deque


def D(n):
    return n * 2 % 10000


def S(n):
    return (n - 1) % 10000


def L(n):
    return n % 1000 * 10 + n // 1000


def R(n):
    return n % 10 * 1000 + n // 10

#! 자료형의 일관성 => 형변환을 최!!대!!로 줄이는 법이 필요하다


def BFS(start, target):
    visited = [False] * 10000
    queue = deque([(start, '')])
    while queue:
        visit, commands = queue.popleft()
        operataion_applied = [
            (D(visit), 'D'), (S(visit), 'S'), (L(visit), 'L'), (R(visit), 'R')]
        for (value, operation) in operataion_applied:
            if not visited[value]:
                #! 여기가 존나 키포인트였다!!!! => 트리 노드를 줄이는 방법!!!!!
                queue.append((value, commands + operation))
                visited[value] = True
        if visit == target:
            print(commands)
            break


N = int(sys.stdin.readline())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    BFS(A, B)
