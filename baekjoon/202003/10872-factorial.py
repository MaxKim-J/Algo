# 백준 10872번 팩토리얼(재귀)
# https://www.acmicpc.net/problem/10872
# 시간 : 13분
# 경과 : 맞았습니다

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

num = int(input())
print(factorial(num))

#! 접근 : 0보다 크거나 같은 수. 0이 들어올때 어떡할것인가를 처리해야함
#* 처리 안 하면 런타임에러 나겟져?