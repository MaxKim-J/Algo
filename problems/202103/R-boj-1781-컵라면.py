# 데드라인을 초과하는 문제는 풀수 없다(설명이 부족함) - 우선순위, 2개를 한꺼번에 풀수 없음
# 정렬과 우선순위 큐 = O(NlogN)
# 데드라인을 기준으로 오름차순 정렬 수행

import heapq

n = int(input())
array = []
q = []

# 문제 정보를 입력받은 이후 데드라인을 기준으로 정렬
for i in range(n):
  a, b = map(int, input().split(' '))
  array.append((a,b))

# 오름차순 정렬
array.sort()

for i in array:
  # 컵라면을 일단 힙큐에 넣음 - 넣을때 가장 최대값인거 (정렬되었으니)
  heapq.heappush(q, i[1])
  # 데드라인 비교하고 데드라인이랑 안맞으면 바로 빼버림
  if i[0] < len(q):
    heapq.heappop(q)

print(sum(q))
