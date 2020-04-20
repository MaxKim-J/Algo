# 백준 11053: 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 시간 : 60분
# 경과 : 틀렸습니다 => 틀렸습니다 => 틀렸습니다 => 못품


n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        # * 이 숫자가 숫자들 중 가장 큰 길이에 들어갈만 하다는 의미
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

#! 자신보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1
#! dp에서 옆에있는 값 그대로 옮겨오고, 자신을 더해줌(+1)

"""
#! 사실 왜틀렸는지 모르겠음;;;;
#! 접근 자체는 거의 비슷함

from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

count = [0]*N
max_val = [0]*N

for i in range(N):
    for j in range(i+1):
        if max_val[j] < A[i]:
            max_val[j] = A[i]
            count[j] += 1

print(max(count))
"""
