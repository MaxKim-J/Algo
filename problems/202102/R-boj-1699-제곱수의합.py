n = int(input())
dp = [0 for i in range(n + 1)]
# 10만의 최대 제곱수...를 할 필요는 없고 그 수 제곱근까지만 돌리면 됨
square = [i * i for i in range(1, int(n ** 0.5) + 1)]

# 1부터 해당 수까지 쭉쭉해서 최소항을 구함
for i in range(1, n + 1):
    tmp = []
    # 제곱수 빠지는 것 중에 가장 작은값 => 점화식 구할 수 있었음 ( dp[i] = min(dp[i-j]) + 1)
    for j in square:
        if j > i:
            break
        tmp.append(dp[i - j])
    dp[i] = min(tmp) + 1

print(dp[n])


'''
DP인듯 아닌 풀이

얘는 Python3로는 통과못할거같음 

무작정 큰 수를 빼는게 답이 아니었다..
이런식으로 모든 경우의 수에서 최소값을 구해줄 수도 있음

import sys 
N = int(sys.stdin.readline()) 
square = [] 
arr = [100000] * (N+1) 

# 제곱수 배열 구하기
for i in range(N + 1): 
    el = i**2 
    if el > N: 
        break 
    square.append(el) 
    arr[el] = 1 

for idx in range(N + 1): 
    for sq in square: 
        if idx < sq: 
            break 
        arr[idx] = min(arr[idx], arr[sq] + arr[idx-sq]) 

sys.stdout.write(str(arr[N]))
'''
