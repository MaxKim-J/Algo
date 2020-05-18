# 백준 1037: 약수
# https://www.acmicpc.net/problem/5086
# 시간 : 20분
# 경과 : 틀렸습니다 => 맞았습니다(60ms)

N = int(input())
real_fraction = list(map(int, input().split()))
real_fraction.sort()

if N % 2 == 0:
    print(real_fraction[0]*real_fraction[-1])
else:
    print(real_fraction[N//2]**2)

# * 처음에 틀린 이유 : 조건에서 모든 약수가 정렬되어서 입력된다는 말이 없었으므로 sort가 필요했다
