n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

# 집들 사이의 거리 중 최소, 최대
start = array[1] - array[0]
end = array[-1] - array[0]

result = 0

while (start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    # 인접한 두 공유기 사이의 *최대* 거리
    # 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치

    # mid가 커진다 => 간격을 키운다(마지막으로 키워졌을 때)
    if count >= c:
        start = mid + 1
        result = mid
    # mid 작아진다 => 간격을 좁힌다
    else:
        end = mid - 1

print(result)
