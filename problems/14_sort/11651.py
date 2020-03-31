import sys

char_num = int(sys.stdin.readline())
arr = []

for _ in range(char_num):
    xy = list(map(int, sys.stdin.readline().split()))
    xy[0], xy[1] = xy[1], xy[0]
    arr.append(xy)

for i, j in sorted(arr):
    print(f"{j} {i}")
