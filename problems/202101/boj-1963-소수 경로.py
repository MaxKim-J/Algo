import sys
from collections import deque
# 오 한번에 풀림 개꿀

# 에라토스테네스 체 구현하는데 애먹었다
# 이정도는 그냥 외우도록 하자...


def prime_list_in_range(n):
    filter = [True] * n

    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if filter[i] == True:
            for j in range(i+i, n, i):
                filter[j] = False

    return [str(i) for i in range(1000, n) if filter[i] == True]


def swap(number, digit, new):
    return number[:digit] + str(new) + number[digit+1:]


def BFS(start, target):
    global primes
    queue = deque([(start, 0)])
    visited = [False] * 10000
    while queue:
        value, depth = queue.popleft()
        if value == target:
            return depth
        for i in range(0, 4):
            for j in range(0, 10):
                if (i == 0) and (j == 0):
                    continue
                new_number = swap(value, i, j)
                if (new_number in primes) and (not visited[int(new_number)]):
                    visited[int(new_number)] = True
                    queue.append((new_number, depth + 1))
    return 'impossible'


N = int(sys.stdin.readline())
primes = prime_list_in_range(9999)
for _ in range(N):
    A, B = sys.stdin.readline().split()
    print(BFS(A, B))
