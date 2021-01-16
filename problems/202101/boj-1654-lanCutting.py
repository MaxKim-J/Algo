K, N = map(int, input().split())
lines = []
for i in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)
result = start
while start <= end:
    mid = (start + end) // 2
    count = 0
    for line in lines:
        count += (line // mid)
    # N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다
    # N개보다 같거나 많이 만들 수 있는 최대 랜선의 개수
    if count >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
