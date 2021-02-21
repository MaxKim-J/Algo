'''
병합정렬할때 그 포인터로 하는 정렬방법
배열을 직접 modify하는건 시간초과나고
가장 빠른 방법은 

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in sorted(A+B):
    print(i, end=' ')

이거였음ㅋ
'''

# 그나마 돌아가는 방법이면서 문제의 의도를 충족하는 해답은 이거임

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

a = 0
b = 0

for _ in range(2000000):
    if a > len(A) - 1:
        result.extend(B[b:])
        break

    if b > len(B) - 1:
        result.extend(A[a:])
        break

    if A[a] > B[b]:
        result.append(B[b])
        b += 1
    elif A[a] <= B[b]:
        result.append(A[a])
        a += 1

for i in result:
    print(i, end=' ')
