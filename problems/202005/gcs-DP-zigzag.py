# 갓찬수 DP: 지그재그 문제
# 시간 : 30분


a = [3, -1, 2, 5, 7, 4, 5, 9, 8]
high, low = [0]*len(a), [0]*len(a)

for k in range(len(a)):
    for j in range(k):
        if a[j] > a[k]:
            low[k] = max(low[k], high[j] + 1)
        if a[j] < a[k]:
            high[k] = max(high[k], low[j] + 1)

print(max(high+low))
