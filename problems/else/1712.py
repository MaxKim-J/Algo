import sys

A, B, C = map(int, sys.stdin.readline().split())

if C <= B:
    print(-1)
else:
    result = A /(C - B)
    print(int(result)+1)