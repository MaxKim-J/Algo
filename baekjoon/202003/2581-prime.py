# 백준 2581번 소수
# https://www.acmicpc.net/problem/2581
# 시간 : 27분
# 경과 : 틀렸습니다 => 맞았습니다 => 맞았습니다 
# 제한시간 : 228/1000 ms => 64/1000 ms

from math import sqrt

def valid_prime(num):
    if num == 1:
        return False
    for lesser in range(2, int(sqrt(num)) + 1):
        if num % lesser == 0:
            return False
    return True

min_num = int(input())
max_num = int(input())

prime_list = [n for n in range(min_num, max_num+1) if valid_prime(n)]
print(sum(prime_list), min(prime_list), sep="\n") if prime_list else print(-1)

#! 틀렸습니다 1 이유 : 1은 소수가 아닌데 넣어서
#* 개선 1 : 1을 거르는 if문 넣음

#* 개선 : 제곱근까지 나눠보는걸로 하면 더 빠르다
'''
n의 제곱근을 기준으로 곱해서 n이 될 수 있는 약수들이 같은 개수로 분포한다
근데 여기서 문제는 10 이하의 숫자들 : 예외처리해준다
개선 알고리즘의 시간 : 64ms - 3배 더 빨라짐
'''