# 백준 14889 : 스타트와 링크
# https://www.acmicpc.net/problem/14889
# 시간 : 60분
# 경과 : 런타임 에러 -> 틀렸습니다 -> 못품
#! 복습 필수

# 이런식으로 하려고 했었는데, DFS for문에서 모든 데이터를 다 순회할 수 없었다
# 결과적으로는 두개를 동시에 뽑아서 진행을 했어야 됐는데, 기존의 포문으로는 못하는듯
from sys import stdin, maxsize

N = int(stdin.readline())
table = []
for _ in range(N):
    table.append(list(map(int, stdin.readline().split())))

min_val = maxsize


def calculate(team, team_mem):
    if len(team_mem) < 2:
        return 0
    result, new_mem = 0, team_mem[-1]
    for mem in team_mem[:-1]:
        result += (table[mem][new_mem] + table[new_mem][mem])
    return result


def DFS(choices, start_mem, link_mem, start, link, count):
    global min_val
    if count == N//2:
        fair_game = abs(start-link)
        print(start_mem, link_mem)
        if fair_game < min_val:
            min_val = fair_game

    else:
        for start_choice in choices:
            choices.remove(start_choice)
            new_start_mem = start_mem+[start_choice]
            for link_choice in choices:
                choices.remove(link_choice)
                new_link_mem = link_mem + [link_choice]

                new_start = calculate(start, start_mem)
                new_link = calculate(link, link_mem)
                print(start_mem, link_mem)
                DFS(choices[:], new_start_mem, new_link_mem,
                    new_start, new_link, count + 1)


choice_list = list(range(0, N))
DFS(choice_list, [], [], 0, 0, 0)
print(min_val)


# todo 답안 1) 내가 처음에 접근했던 것처럼 풀었던 답안(다른점이 있따면 itertool)
"""
#! 결국 이터툴로 해야만 파이썬에서는 시간에 맞출 수 있었음
#! product가 중복 가능한 순열을 만드는 메소드였다면 combination은 조합을 만든다
from itertools import combinations

N = int(input())
ability_board = []
for _ in range(N):
    ability_board.append(list(map(int, input().split())))

num_list = [i for i in range(N)]
res = float('inf')

def solve():
    global res
    
    #! 조합을 이용하여 각 후보자를 생성함, 8c4로 뽑을 수 있는 모든 경우의수를 비교
    for cand in combinations(num_list, N // 2):
        #! 선택된 후보와 나머지로 팀을 가른다 feat 집합
        #* 이 방법도 생각을 안해본건 아닌데 재귀를 돌려야한다는 생각에 커서
        #* 재귀 과정에서 계산이 이루어지는 걸 원했기 때문에 이렇게 못함
        #* 하지만 이터툴의 속도라면? ㅆㄱㄴ이었다고 한다
        start_member = list(cand)
        link_member = list(set(num_list) - set(cand))
        
        #! 여기서도 조합을 구해버린다 그렇게 조합을 두번 구한다..
        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))
        
        #! 점수 구하기
        start_sum = 0
        #* 조합 리스트를 돌리면서 계산한다
        for x, y in start_comb:
            start_sum += (ability_board[x][y] + ability_board[y][x])
            
        link_sum = 0
        for x, y in link_comb:
            link_sum += (ability_board[x][y] + ability_board[y][x])
        
        #! 차이를 구하는 것이므로 abs 사용
        if(res > abs(start_sum - link_sum)):
            res = abs(start_sum - link_sum)
            
solve()
print(res)
"""

# todo 답안 2) 매우 빠른 답안(62ms)인데 좀 난해하다
# * 나올수 있는 모든 스탯 자체를 먼저 계산한 것으로 보임
"""
import sys
from itertools import combinations as cb

N = int(sys.stdin.readline()) // 2
M = 2*N

#* 이차원 배열 받고
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#* 이차원배열의 행렬값을 각각 더해서 리스트를 만들었다(???)
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]

#* 굳이 이렇겐 왜했지
newstat = [i+j for i, j in zip(row, col)]
allstat = sum(newstat) // 2

newstat.sort()
newstat[1::2] = newstat[-1::-2]

allstat -= newstat[-1]

mins = 65535

for l in cb(newstat[:-1], N-1):
    mins = min(mins, abs(allstat - sum(l)))
    if not mins:
        print(0)
        break
else:
    print(mins)
"""
