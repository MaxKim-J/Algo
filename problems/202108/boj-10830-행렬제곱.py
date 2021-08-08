# 타이트하게, 필요한 계산만 하기

import sys
N,B=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
 
def matric_mul(A,B):
    if B==1:
        for i in range(N):
            for j in range(N):
                A[i][j]%=1000
        return A
 
    elif B%2==1:
        tmp=[[0 for _ in range(N)] for _ in range(N)]
        C=matric_mul(A,B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*A[k][j] # 하나를 그냥 더 곱해준다
                tmp[i][j]%=1000
 
        return tmp
 
    else:
        tmp=[[0 for _ in range(N)] for _ in range(N)]
        C=matric_mul(A,B//2) # 2로 나눠지면 쪼개는게 가능하다
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*C[k][j] # 제곱을 때린다
                tmp[i][j]%=1000
        return tmp
 
result=matric_mul(A,B)

for li in result:
    for p in li:
        print(p,end=' ')
    print()


'''
음... 분할정복이라는 키워드는 잘 잡았고 제곱으로 해결한다는 아이디어는 비슷한데
시간초과가 계속 났다.,,,좀더 타이트하게 분할할 수 있어야 한다
이 풀이 같은 경우는 계속 맞는 경우를 대조하기 위해 하향식으로 계속 A부터 제곱수까지 구하기 때문에
시간이 좀더 걸리는 케이스

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]

def mul(x,y):
  new_matrix = []
  for i in range(n):
    row = []
    for j in range(n):
      elem = 0
      for p in range(n):
        elem += (x[i][p] * y[p][j])
      row.append(elem)
    new_matrix.append(row)
  return new_matrix

cache = {}

def mul2(target):
  val = matrix
  num = 1

  if target == 1:
    return val, num

  while True:
    if num > target:
      return cache[num//2], num // 2
    num *= 2
    if cache.get(num):
      val = cache[num]
    else:
      val = mul(val, val)
      cache[num] = val

result = None
while b > 0:
  res, sub = mul2(b)
  result = mul(result, res) if result != None else res
  b -= sub

print(cache)

for row in result:
  for elem in row:
    print(elem % 1000, end=' ')
  print()
'''