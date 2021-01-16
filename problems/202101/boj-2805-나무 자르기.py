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
    # "적어도 M미터의 나무를 집에 가겨지기 위한 절단기 높이의 최대값"
    if total_log <= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
