# 백준 2580 : 연산자 끼워넣기
# https://www.acmicpc.net/problem/2580
# 시간 : 50분
# 경과 : 시간초과 => 시간초과 => 맞았습니다(2520ms - pypy3)
#! 복습 필수

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
operands_input = map(int, sys.stdin.readline().split())

operands = []
min_val, max_val = sys.maxsize, -sys.maxsize

for idx, num in enumerate(operands_input):
    operands += [idx]*num


def calculate(default, new, operand):
    if operand == 0:
        return default + new
    elif operand == 1:
        return default - new
    elif operand == 2:
        return default * new
    else:
        if default < 0:
            return -(abs(default) // new)
        else:
            return default//new


def DFS(operands, current_result, count):
    global min_val, max_val
    if count == N-1:
        result = num_list[0]
        for i in range(N-1):
            new = num_list[i+1]
            result = calculate(result, new, current_result[i])
        if result < min_val:
            min_val = result
        if result > max_val:
            max_val = result
    else:
        for operand in operands:
            new_operands = operands[:]
            new_operands.remove(operand)
            DFS(new_operands, current_result + [operand], count + 1)


DFS(operands, [], 0)
print(max_val)
print(min_val)

#! 시간이 넘 느린 원인 1) 모든 경우의 수를 구하고 그 다음에 몰아서 연산을 하도록 코드를 짰는데 너무 오래 걸린다
# * 경우의 수를 구함과 동시에 그때까지의 연산 결과는 충분히 할 수 있었다
#! 시간이 넘 느린 원인 2) 최소 최대값 구할때 리스트 min으로 구하지 말자;;
# * 혹시나 했는데 200ms 넘게 줄더라 최소 최대값은 저렇게 괄호로 그때그때 구하자 내가 불편하면 코드가 빨라진다;
#! !!!!!!!!!!!!!미루지 말고 그때그때 구하자!!!!!!!!!!!!!!(매우 중요)
# * 연산을 같이 할 수 있는건 같이 해야댐!!!!!! 연산을 잘 끼워넣고, 연산에 필요한 정보들을 확인하자

"""
#! 괜찮다고 생각했던 풀이(python3 - 62ms)

from sys import stdin

def calc(num, p, s, m, d, k=1):
    global min_num, max_num
    #! 그 많던 재귀함수들은 모두 여기서 모이고 전역변수를 업데이트하게 됨
    if k == N:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
        return True

    nxt = numbers[k]
    #! 모두 거쳐야하는 if문으로 재귀를 만들어낸다
    #!!!!!!! 이렇게 다른 뎁쓰의 재귀함수를 부를때 연산 한 값을 또 넘긴다. 재귀호출과 동시에 값을 연산하고 있다
    if p > 0:
        calc(num+nxt, p-1, s, m, d, k+1)
    if s > 0:
        calc(num-nxt, p, s-1, m, d, k+1)
    if m > 0:
        calc(num*nxt, p, s, m-1, d, k+1)
    if d > 0:
        calc(int(num/nxt), p, s, m, d-1, k+1)


N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
plus, sub, mul, div = list(map(int, stdin.readline().split()))
cur = numbers[0]
min_num = 10 ** 9
max_num = (10 ** 9) * -1
calc(cur, plus, sub, mul, div)

print(max_num)
print(min_num)
"""


# * 일단 쳐내는거 없고 모든 경우의 수를 다 해봐야 한다는건 맞았음. 굳이 따지자면 백트랙킹 문제보다는 브루트 포스에 더 가까움
