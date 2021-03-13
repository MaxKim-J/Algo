# 일직선상의 각 책들을 원래의 위치에 놓기
# 0보다 큰 책들과 0보다 작은 책들을 나누어 처리
# M개씩의 묶음(한번에 들 수 있는 책 권수) 중 가장 거리가 먼 책만큼 이동해야함 - 합리적
# 가장 먼 편도거리를 뺌 - 마지막으로 옮기는 책은 이동만 하면 되고 돌아올 필요가 없음(가장 먼거)

import heapq

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), - min(array))

for i in array:
  if i > 0:
    heapq.heappush(positive, -i)
  else:
    heapq.heappush(negative, i)

result = 0

# m개씩 빼내기
while positive:
  result += heapq.heappop(positive)
  for _ in range(m-1):
    if positive:
      heapq.heappop(positive)

while negative:
  result += heapq.heappop(negative)
  for _ in range(m-1):
    if negative:
      heapq.heappop(negative)

print(-result * 2-largest)