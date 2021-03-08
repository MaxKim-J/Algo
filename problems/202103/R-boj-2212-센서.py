# 최대 K개의 집중국 => 수신 가능 영역의 길이의 합을 최소화
# 사실상 정렬만 수행하면 됨 => 정렬된 센서들을 최대 K개의 영역으로 나누는 것
# 그리디하게 작은 값부터 크기를 나눠야함
# 센서 사의의 거리를 계산한 후 가장 머리가 먼 순서대로 k-1개의 연결고리 제거 => 유니언 박살
# 가장 거리가 긴 순서부터 제거

n = int(input())
k = int(input())

if k >= n:
  print(0)
  exit(0)

array = list(map(int, input().split(' ')))
array.sort()

distances = []

# 각 센서간의 거리 계산하여 내림차순으로 정렬 
for i in range(1,n):
  distances.append(array[i] - array[i-1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거, 기지국 개수만큼
for i in range(k-1):
  distances[i] = 0

print(sum(distances))

# 딱 떨어지는 그리디..