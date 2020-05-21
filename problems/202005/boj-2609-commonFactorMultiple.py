# 백준 2609: 최대공약수 최소공배수
# https://www.acmicpc.net/problem/2609
# 시간 : 15분
# 경과 : 틀렸습니다 => 맞았습니다(60ms)


a, b = map(int, input().split())
i = 2
fraction = 1

while not((i > a) or (i > b)):
    if (a % i == 0) and (b % i == 0):
        a //= i
        b //= i
        fraction *= i
    else:
        i += 1

print(fraction)
print(fraction*a*b)

#! 약수와 관련된 문제
# * 1. 작은수부터 위로 올라가면서 검증해도 무방
# * 2. 약수 관련된것들은 제곱근 까지만 반복해도 무방
