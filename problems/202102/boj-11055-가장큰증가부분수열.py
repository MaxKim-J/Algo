n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    max_value = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_value = max(max_value, dp[j])
    dp.append(arr[i] + max_value)

print(max(dp))
