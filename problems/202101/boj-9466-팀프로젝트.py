import sys
testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n = int(sys.stdin.readline())
    choice = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [0] * (n+1)
    group = 1
    for i in range(1, n+1):
        if visit[i] == 0:
            while visit[i] == 0:
                visit[i] = group
                i = choice[i]
            while visit[i] == group:
                visit[i] = -1
                i = choice[i]
            group += 1
    cnt = 0
    for v in visit:
        if v > 0:
            cnt += 1
    sys.stdout.write("{}\n".format(cnt))

'''
from collections import defaultdict

T = int(input())


def search(start):
    global team_matched
    visited = defaultdict(int)
    current = dag[start]
    while True:
        if current == start:
            visited[start] = 1
            for i in visited.keys():
                team_matched[i] = True
            return
        if visited[current] == 0:
            visited[current] = 1
            current = dag[current]
        else:
            return


for _ in range(T):
    N = int(input())
    team = list(map(int, input().split()))
    dag = {i+1: team[i] for i in range(N)}
    team_matched = {i+1: False for i in range(N)}
    for j in range(N):
        if team_matched[j+1] == False:
            search(j+1)

    ans = 0
    for i in team_matched.values():
        if i == False:
            ans += 1
    print(ans)
'''
