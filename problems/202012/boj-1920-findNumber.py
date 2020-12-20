import sys

a_length = sys.stdin.readline()
a_arr = list(map(int, sys.stdin.readline().split(' ')))
b_length = sys.stdin.readline()
b_arr = list(map(int, sys.stdin.readline().split(' ')))

answer = [0] * int(b_length)
frequency_dict = dict()
print(a_arr, b_arr)

for (idx, elem) in enumerate(b_arr):
    frequency_dict[elem] = idx

for elem in a_arr:
    if(elem in frequency_dict):
        answer[frequency_dict[elem]] = 1

for i in answer:
    print(i)


'''
이분탐색으로 풀어도 무방하다

// 동빈나 풀이
a_length = sys.stdin.readline()
a_arr = set(map(int, sys.stdin.readline().split(' ')))
b_length = sys.stdin.readline()
b_arr = list(map(int, sys.stdin.readline().split(' ')))

for i in b_arr:
    if i not in a_arr:
        print('0')
    else:
        print('1')
'''
