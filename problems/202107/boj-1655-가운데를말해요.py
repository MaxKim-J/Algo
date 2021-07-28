# 더더더더더 단순하게 생각하고 더더더더 머리를 굴리기
# sys를 안쓰면 통과가 안됨

import heapq
import sys

left, right = [], []

n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())
  # 일단 다 넣는다
  if (len(left) == len(right)):
    heapq.heappush(left, (-num, num)) # maxheap
  else:
    heapq.heappush(right, (num, num)) # minheap

  # 다 넣고 조건이 위배되는 상황만 체크하면서 맞는 배열을 만든다
  # 왼쪽의 최소값이 오른쪽 값보다 큰 경우 => 왼쪽과 오른쪽 최소값을 바꿔치기함
  # 아...mid를 상정한게 에바였다..
  if len(right) >= 1 and len(left) >= 1 and left[0][1] > right[0][1]:
    left_value = heapq.heappop(left)[1]
    right_value = heapq.heappop(right)[1]
    heapq.heappush(right, (left_value, left_value))
    heapq.heappush(left, (-right_value, right_value))

  print(left[0][1])

'''
import heapq # 이진탐색으로 삽입삭제할수도 있을듯함
import sys 

N = int(sys.stdin.readline())

left = [] # min heap임!
right = []
mid = -10001

for i in range(1, N+1):
  num = int(sys.stdin.readline())
  if (mid == -10001):
    mid = num
    print(mid)
    continue

  if (i % 2 == 0):
    if num >= mid:
      heapq.heappush(right, num)
    else:
      heapq.heappush(left, num)
      mid = left.pop()
      right.insert(0, mid)
  else:
    if num >= mid:
      heapq.heappush(right, num)
      if (len(right) == len(left)):
        print(mid)
        continue
      heapq.heappush(left, mid)
      mid = right.pop(0)
    else:
      heapq.heappush(left, num)
      if (len(right) == len(left)):
        print(mid)
        continue
      heapq.heappush(right, mid)
      mid = left.pop()

  print(mid)

'''