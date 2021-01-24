from collections import defaultdict  # 이거 속도 쵸큼 떨어지긴 하는데 좋은듯?


T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

memo = defaultdict(int)

count = 0


def solve(length, arr, id):
    global count, memo
    # 조합을 구하는 포문 => 대충 O(n^2 + m) 정도로 돌아간다
    for i in range(length):
        for j in range(length-i):
            sum_value = 0
            for m in range(i+1):
                sum_value += arr[m+j]
            if id == 'A':
                memo[sum_value] += 1
            elif id == 'B':
                if memo[T-sum_value]:
                    count += memo[T-sum_value]


solve(N, A, 'A')
solve(M, B, 'B')

print(count)
