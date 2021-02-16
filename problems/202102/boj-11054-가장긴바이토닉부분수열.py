n = int(input())
arr = list(map(int, input().split()))
arr2 = list(reversed(arr[:]))


def get_dp(arr):
    dp = [1]
    for i in range(1, n):
        max_value = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_value = max(max_value, dp[j])
        dp.append(max_value + 1)
    return dp


dp1 = get_dp(arr)
dp2 = get_dp(arr2)
dp2.reverse()

max_value = 0
for i in range(n):
    max_value = max(max_value, dp1[i] + dp2[i])

print(max_value - 1)
