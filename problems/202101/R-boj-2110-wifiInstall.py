# 가장 인접한 두 공유기 사이의 최대 거리를 이진 탐색으로 찾는 문제임 => log
# x의 범위가 10억까지이므로 선형 탐색으로는 문제를 풀 수 없다

# 이진탐색은 Min과 max를 찾고 그 중간값을 계속 반복하는 것 => 꼭 선형 데이터일 필요가 없다
# 그 중간값으로 공유기 사이의 거리를 설정하고, 순회를 하면서 공유기를 설치했는데 n개가 아니면 한번더 탐색
# n개가 아니면 갭을 늘리거나 줄인다. c보다 작으면 줄이고(이하로 이분탐색) 크면 늘인다(이상으로 이분탐색)
#! 그니까 어떤 데이터들 사이에서 탐색을 할것인지 설정할 수 있어야 함 보이는 것만 보지 말쟈...
#! 약간 정답지향적 이분탐색이라고 해야하나...

n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

# 거리의 값을 최대와 최소로 설정
start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while (start <= end):
    # 여기서 mid는 바로 그 갭이다, 우리는 거리를 찾고 있음
    # 가능한 거리의 범위는 선형적임 선형적인 데이터 위에서 이분탐색
    mid = (start + end) // 2
    value = array[0]
    count = 1
    # 배열 순회
    for i in range(1, len(array)):
        # 공유기 설치 해봄
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    # 카운트랑 목표를 비교
    # c개 이상의 공유기를 설치할 수 있는 경우
    if count >= c:
        # 그거보다 밑 값은 이제 볼필요도 없음 => 갭을 늘려도 공유기 설치 가능한지 확인
        start = mid + 1
        # 일단 저장하고 더 최대 거리로 공유기 설치 가능한지 다시 확인
        result = mid
    # c개 이상의 공유기를 설치할 수 없는 경우
    # 그거 이상 거리로는 이제 볼필요도 없다 => 갭을 줄여서 설치하는 공유기 개수를 늘리려는 시도
    else:
        end = mid - 1

print(result)
