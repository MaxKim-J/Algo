# 백준 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
#! 복습 : 수 범위가 주어졌을 때 계수정렬을 이용하면 좀 더 빠른 정렬이 가능함

# *그냥 sort 메소드 쓰면 메모리가 초과됨(;)

"""
N = int(input())
sort_arr = []
for _ in range(N):
    num = int(input())
    sort_arr.append(num)

sort_arr.sort()

for i in sort_arr:
    print(i)
"""

# *계수정렬을 해보자. 숫자가 정해져 있을 땐 더 빠르다
# 이렇게 코드 바꾸고 재체점(10468ms => 5604ms)
import sys

N = int(sys.stdin.readline())
sort_arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    sort_arr[num] += 1

# 자기 인덱스 값이랑 인덱스를 곱한 만큼 인쇄하면 되니까 요래도 된다(if통과 안시키니 더 빨라짐)
# 한줄씩 출력시킬때 한번 고려해볼만한 코드다
for i in range(1, 10001):
    print(f"{i}\n"*sort_arr[i], end="")

# ? open()을 이용해서 백준 인풋을 한꺼번에 받아들인 후 for문으로 순회할 수 있는 것 같은데 방법 찾아보기
