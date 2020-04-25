# 백준 1912: 연속합
# https://www.acmicpc.net/problem/1912
# 시간 : 60분+
# 경과 : 시간초과 => 시간초과 => 맞았습니다


N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]
for i in range(len(A) - 1):
    dp.append(max(dp[i] + A[i + 1], A[i + 1]))
print(max(dp))

#! 진짜 개쓸데없이 해매다가 오래걸림
#! 접근1) 연속된 합을 구하는거니깐 그냥 뒷값이랑 비교했을 때 누적된 합이랑 그 다음 값중에 더 큰값이 뭔지 비교하면 됨
#! 접근2) 포문으로 돌릴때, 한번의 순회는 배열 요소가 거기까지 있을 때 연속합의 최대값 => 그 전 순회 연속합 최대값에서 새로운 값만 고려하면 된다
