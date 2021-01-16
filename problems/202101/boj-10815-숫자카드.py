N = int(input())
cards = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

cards.sort()
sorted_finds = sorted(finds)

start_memo = 0
result = dict()

# start 값을 갱신하는 이분탐색
#! 둘다 정렬하고 만약에 수를 찾았다면 그 인덱스 이하는 이제 하나도 안쳐다봐도 된다는거 이용
for find in sorted_finds:
    # 이분탐색 하기 전에 이전에 기록된 start를 저장
    prev_start = start_memo

    # 이분탐색 시작. 기록된 start를 바탕으로 시작
    start = start_memo
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] <= find:
            start = mid + 1
            # 답을 찾았다면 그 값을 start_memo에 저장
            start_memo = mid
        else:
            end = mid - 1
    # start_memo를 평가
    if cards[start_memo] == find:
        result[find] = 1
    else:
        result[find] = 0
        # 카드에 없다면 이전 prev_start를 다음 루프에서도 그대로 가져감
        start_memo = prev_start

for find in finds:
    print(result[find], end=' ')
