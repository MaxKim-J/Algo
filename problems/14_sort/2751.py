import sys


# def quick_sort(a, start, end):
#     if start < end:
#         left = start
#         pivot = a[end]
#         for i in range(start, end):
#             if a[i] < pivot:
#                 a[i], a[left] = a[left], a[i]
#                 left += 1
#         a[left], a[end] = a[end], a[left]
#         quick_sort(a, start, left-1)
#         quick_sort(a, left+1, end)


num_arr = []
char_num = int(sys.stdin.readline())
for _ in range(char_num):
    input_num = int(sys.stdin.readline())
    num_arr.append(input_num)

num_arr.sort()

for elem in num_arr:
    print(elem)
