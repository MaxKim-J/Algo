# 수 정렬하기

import sys


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_idx = i
        for j in range(0, i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


num_arr = []
char_num = int(sys.stdin.readline())
for _ in range(char_num):
    input_num = int(sys.stdin.readline())
    num_arr.append(input_num)

for char in selection_sort(num_arr):
    print(char)
