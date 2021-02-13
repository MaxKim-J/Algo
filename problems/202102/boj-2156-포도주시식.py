# 점화식은 잘 짰는데... 메모리 넘침

n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))
dp = [0]
dp.append(wine[1])
if n > 1:
    dp.append(wine[1] + wine[2])
for i in range(3, n + 1):
    # 항상 새로운 값은 wine배열에서 가져온다 => 메모리 아끼기
    dp.append(max(dp[i - 1], dp[i - 3] + wine[i - 1] +
                  wine[i], dp[i - 2] + wine[i]))
print(dp[n])

# n = int(input())
# glass = []
# for _ in range(n):
#     glass.append(int(input()))
# dp = [glass[:] for _ in range(2)]

# dp[0][1] += dp[0][0]
# dp[1][2] += max(dp[1][0], dp[0][1])

# for i in range(3, n):
#     temp = dp[i-1][:]
#     temp_num = max(dp[i-2][i-1] + dp[i-2][i-3], dp[i-1][i-2])
#     temp[i] += temp_num
#     dp.append(temp)

# print(max(dp[n-1]))
