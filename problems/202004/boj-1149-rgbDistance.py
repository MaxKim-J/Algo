# 백준 1149: RGB거리
# https://www.acmicpc.net/problem/1149
# 시간 : 60분 초과
# 경과 : 틀렸습니다 -> 못품

import sys

N = int(sys.stdin.readline())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, len(houses)):
    houses[i][0] = min(houses[i - 1][1], houses[i - 1][2]) + houses[i][0]
    houses[i][1] = min(houses[i - 1][0], houses[i - 1][2]) + houses[i][1]
    houses[i][2] = min(houses[i - 1][0], houses[i - 1][1]) + houses[i][2]
print(min(houses[N - 1][0], houses[N - 1][1], houses[N - 1][2]))

#! 접근 자체는 잘 했다. 맨 앞이 빨,초,파 인 경우중에 최소값을 구하면 되는건데
#! 약간 백트랙킹 처럼 코드를 짠듯. 게다가 틀렸습니다 나왔는데 왠지 모르겟음;
#! 트리식으로 모든 경우를 트래킹해야하나 싶고 자신감이 좀 없었던 것 같음 => 그러면 그방법은 노노
"""
for i in range(3):
    temp, former_color = houses[0][i], i
    for idx in range(1, N):
        house = houses[idx][:]
        house[former_color] = 1000
        new_val, former_color = min(zip(house, range(3)))
        temp += new_val
    if temp < min_val:
        min_val = temp

print(min_val)
"""
#! 동적 계획법은 시간과 메모리를 줄여야 하므로, 메모리는 가급적 원래 있었던거 활용하자
#! 시간은 앞값과 뒷값을 어떻게 이용할 수 있는지 생각해봐야 함, 가난하게 풀자!
# 업데이트를 하는 과정은 아래와 같다. : 반대로 생각해야 이해할 수 있음
#! 배열에서 갱신되는 값은 그 집에 색을 칠했을 때 소요되는 최소비용(앞에 무슨 색 칠했는지 고려)
#! 메모이제이션이 트래킹을 이길 수 있다 무슨 값을 저장해야되는지 생각하자
"""
1. 각 샐은 현재 집을 해당 컬럼(R,G,B)로 칠했을때의 최소 비용이다.

2.  집2에 빨간색을 칠하는 경우 : 집2를 빨간색으로 칠하는 비용 + 최소값(집1을 초록색으로 칠하는 경우, 집 1을 파란색으로 칠하는 경우)
    집2에 파란색을 칠하는 경우 : 집2를 파란색으로 칠하는 비용 + 최소값(집1을 초록색으로 칠하는 경우, 집 1을 빨간색으로 칠하는 경우)

위 2개의 규칙을 따라서 전체 셀을 업데이트 한다.
"""
