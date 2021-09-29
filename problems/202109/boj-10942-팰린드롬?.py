'''
진짜 개에바 문제다 sys를 안써서 틀렸습니다만 오지게 찍혔다
백준에서 파이썬으로 풀때, 입력이 백만개 천만개 이러면 sys를 꼭 쓰도록 하자

일단 짝수, 홀수 팰린드롬을 만들때 i-2번째 행을 참조하는 방법으로 점화식을 구성했다
근데 이렇게되면 DP 테이블이 순서대로 채워지지는 않아서 꽤 직관적이지 않은 방식이지만
모든 상황에 대한 DP값을 다 구한다는 점에서 아래 풀이와 시간상으로 크게 차이나지는 않는다
'''

#? 내풀이

import sys
input = sys.stdin.readline

N = int(input())
order=list(map(int, input().split()))
M = int(input())

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N): # 간격
  for j in range(1, N-i+1): # 시작점
    if i == 0 or i == 1: # dp[1], dp[2] 채워넣기
      if order[j-1] == order[j+i-1]:
        dp[j][j+i] = 1
    else:
      if (dp[j+1][j+i-1] == 1) and (order[j-1] == order[j+i-1]):
        dp[j][j+i] = 1

for _ in range(M):
  s,e = map(int, input().split())
  print(dp[s][e])

#* 남의풀이

'''
팰린드롬 DP의 정석대로, 테이블의 좌우를 문자열의 인덱스로 채워 놓는 방식이다
dp[1][4]가 팰린드롬인지 알려면 dp[2][3]이 팰린드롬인지 먼저 알아야 되는 식이다.
'''

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len
   
        if start == end:
            dp[start][end] = 1

        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
            

for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])