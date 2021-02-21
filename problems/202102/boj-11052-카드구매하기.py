n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0, arr[1]]

for i in range(2, n+1):
    tmp = arr[i]
    for j in range(i-1, 0, -1):
        tmp = max(dp[j] + arr[i-j], tmp)
    dp.append(tmp)

print(dp[-1])
