n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


if n < 3:
    print(sum(arr))
    exit(0)

dp = [arr[0], arr[0] + arr[1],  max(arr[0] + arr[2], arr[1] + arr[2])]

for i in range(3, n):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp[-1])
