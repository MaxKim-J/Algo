# 백준 2748 : 피보나치 수 2
# https://www.acmicpc.net/problem/2748
# 시간 : 10분
# 경과 : 맞았습니다(60ms)

n = int(input())
pibo_arr = [0, 1]
for i in range(n-1):
    pibo_arr.append(pibo_arr[i] + pibo_arr[i+1])

print(pibo_arr[-1])

# * DP의 아주 기본 문제, if 쓰기 싫어서 리스트에 넣고 시작했음
