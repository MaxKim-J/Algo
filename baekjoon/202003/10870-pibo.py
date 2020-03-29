# 백준 10870번 피보나치(재귀)
# https://www.acmicpc.net/problem/10870
# 시간 : 4분
# 경과 : 맞았습니다


def pibo(n):
    if n == 0 or n == 1:
        return n
    return pibo(n-1) + pibo(n-2)


num = int(input())
print(pibo(num))

# * 앞문제랑 거의 똑같은데 뭐 재귀는 나름 잘 하는듯?
