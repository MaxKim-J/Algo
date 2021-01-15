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
    if count >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
