# 백준 1904: 01타일
# https://www.acmicpc.net/problem/1904
# 시간 : 25분
# 경과 : 틀렸습니다 -> 맞았습니다(296ms)


import sys
num = int(sys.stdin.readline())
start, add, tmp = 1, 2, 0

for i in range(num - 1):
    tmp = start
    start = add
    add = (tmp + add) % 15746
print(start)


#! 계차수열 문제인줄 알았는데 그냥 피보나치 문제였다....
#! 경우 찾아서 노가다 뛰어보면 알 수 있었는데 멍청하게 그걸 잘 못했따,,,
