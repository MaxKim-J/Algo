# 이런거는 일단 무슨 양상으로 채워질 수 있는지 죄다 생각해내는게 중요함
# 이건 좀 그 최소단위를 생각하기가 까다로웠음
# i - j생각하는게 좀..
# DP 시작할 번호가 붕 뜨면 의심을 좀...

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3
for i in range(4, 31, 2):
    # 2개 채울수 있는 3개짜리 * 3
    dp[i] = dp[i - 2] * 3

    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    # 새로운 모양 + 2
    dp[i] += 2
print(dp[n])

'''
더 직관적

import sys 

N = int(sys.stdin.readline()) 
cases = [0] * 31 
cases[2] = 3 

for i in range(4, N+1, 2): 
  cases[i] = 2 + cases[i-2] * 3 + sum(cases[:i-2]) * 2 
  
sys.stdout.write(str(cases[N]))
'''
