# 1920 수 찾기
# 순차탐색보다 훨!씬 빠르다 ㄹㅇ..

import sys


def binary_search(arr, key):
    start, end = 0, len(arr)-1
    while end >= start:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key == arr[mid]:
            return 1
        else:
            start = mid + 1
    return 0


data_num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
find_num = int(sys.stdin.readline())
find_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

for key in find_list:
    print(binary_search(num_list, key))
