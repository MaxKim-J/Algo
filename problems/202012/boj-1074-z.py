# -*- coding: utf-8 -*-


def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n/2, x, y)
    solve(n/2, x, y + n / 2)
    solve(n/2, x + n/2, y)
    solve(n/2, x + n/2, y + n/2)


result = 0
N, X, Y = map(int, input().split(' '))
solve(2**N, 0, 0)


# Z 모양을 구성하는 4가지 방향에 대하여 재귀적으로 호출
# 포인트를 잡아주기 => 0,0으로 순회하고, 실질적으로 순회를 세는거는 맨 마지막까지 쪼개졌을 때
# 재귀를 부르는 순서와 인자도 중요하다 => 맨 위 왼칸부터 부르기, 맨 마지막까지 쪼개질 때까지
# 단순하게 생각하고, 이상한 연산이 많이 나오면 망한거라고 생각해도 좋을듯 하다
