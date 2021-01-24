# 부분수열 합이랑 똑같은 아이디어
#! 자료형을 임의로 나눠 시간을 줄이는 간단하고도 명쾌한 방법!!!!!!!!
#! n^4에는 당연히 못풀고 O(2n^2) 쯤으로 시간을 줄이는 방법이다. 이렇게 백트랙킹도 가능한듯

# 입력이 최대 4 * 4000이니 sys를 사용하자
import sys

N = int(sys.stdin.readline())

answer = 0
A = B = C = D = []

for _ in range(N):
    a1, b1, c1, d1 = map(int, input().split(" "))
    A.append(a1)
    B.append(b1)
    C.append(c1)
    D.append(d1)

AB = dict()

# 전에 풀었던 문제처럼, 합을 완성할때 값을 도출시키면 시간이 더 준다

# 곱경우 구하기
for i in range(N):
    for j in range(N):
        temp = A[i] + B[j]
        if temp in AB:
            AB[temp] += 1
        else:
            AB[temp] = 1

for i in range(N):
    for j in range(N):
        temp = -(C[i] + D[j])
        if temp in AB:
            answer += AB[temp]


print(answer)
