N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = start

while start <= end:
    mid = (start + end) // 2
    total_log = 0
    for tree in trees:
        total_log += max(tree - mid, 0)
    #! 왜 값을 이 시점에 저장하는가
    if total_log <= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
