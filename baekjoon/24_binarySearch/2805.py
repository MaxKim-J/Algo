import sys

K, N = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    slices = 0
    for tree in trees:
        if tree >= mid:
            slices += (tree - mid)
    # 탐색의 범위를 줄여야 한다는 것을 명심!!
    if slices >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
