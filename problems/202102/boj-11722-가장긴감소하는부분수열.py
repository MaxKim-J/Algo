n = int(input())
arr = list(map(int, input().split()))
dp = [1]

for i in range(1, n):
    max_value = 0
    for j in range(i):
        if arr[i] < arr[j]:
            max_value = max(max_value, dp[j])
    dp.append(max_value + 1)

print(max(dp))
