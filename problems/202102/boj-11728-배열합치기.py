'''
오히려 이게 시간초과가 나고
sorted 사용하는게 시간초과가 안난다(...?)
'''


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

for _ in range(2000000):
    if len(A) == 0:
        for j in B:
            result.append(j)
        break

    if len(B) == 0:
        for j in A:
            result.append(j)
        break

    if A[0] > B[0]:
        result.append(B.pop(0))
    elif A[0] <= B[0]:
        result.append(A.pop(0))

for i in result:
    print(i, end=' ')
