# 버블정렬 이용 - 시간초과
# n = len(arr)
# for i in range(n-1, 0, -1):
#     for j in range(0, i):
#         if arr[j + 1][0] < arr[j][0]:
#             arr[j + 1], arr[j] = arr[j], arr[j + 1]
#         elif arr[j + 1][0] == arr[j][0]:
#             if arr[j + 1][1] < arr[j][1]:
#                 arr[j + 1], arr[j] = arr[j], arr[j + 1]

# for xys in arr:
#     print(f"{xys[0]} {xys[1]}")

# 그냥 내장메소드 쓰자
import sys

char_num = int(sys.stdin.readline())
arr = []

for _ in range(char_num):
    xy = tuple(map(int, sys.stdin.readline().split()))
    arr.append(xy)

for i, j in sorted(arr):
    print(f"{i} {j}")
