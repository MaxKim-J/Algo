'''
그때그때 유연한 사고방식으로 문제를 풀 수 있게 준비하자!!!
처음의 우려와는 달리 BFS+백트랙킹으로 해도 괜찮았던 문제였다

다만 BFS 돌때마다 매번 combination을 구해주는 로직을 한번만 해주도록 최적화하고
연산을 K번 할 수 없는 경우도 고려가 필요했음 
'''

from collections import deque
from itertools import combinations
import sys, copy

input = sys.stdin.readline

def bfs():
    visited = set() # 오히려 집합을 쓰는게 메모리를 덜 쓰는 방법일수도 잇겟다
    ans = 0
    qlen = len(q)
    while qlen:
        x = q.popleft()
        cs = str(x)
        for i, j in d:
            s = cs[:i] + cs[j] + cs[i+1:j] + cs[i] + cs[j+1:]
            if s[0] == '0':
                continue
            nx = int(s)
            if nx not in visited:
                ans = max(ans, nx)
                visited.add(nx)
                q.append(nx)
        qlen -= 1
    return ans

n, k = map(int, input().split())
item = [i for i in range(len(str(n)))]

d = list(combinations(item, 2)) #! 어짜피 계속 반복할꺼면 최초 한번 그냥 구해놓기
q = deque() # 큐를 바깥에다가 유지하는 것도 좋네...굳이 포문을 하나 더하지 않아도
# 밖으로 빼서 매 스탭마다 확인이 가능해진다
q.append(n)

ans = 0
while k:
    ans = bfs()
    k -= 1

if not ans:
    print(-1) # 연산을 K번 할 수 없을때 1000, 10000
else:
    print(ans)