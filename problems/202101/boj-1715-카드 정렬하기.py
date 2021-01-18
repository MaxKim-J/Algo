# 가장 크기가 작은 숫자 카드 묶음들을 먼저 합쳤을 때 비교 횟수가 가장 적음
# 가장 크기가 작은 숫자 묶음들을 2개씩 합치기 위해 힙 자료구조 이용

# 힙에다가 일단 다 넣은 후 최소값 두개를 빼서 더한 값을 다시 힙에 넣는다 => 힙에 숫자가 하나 나올때까지 그걸 반복

import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
