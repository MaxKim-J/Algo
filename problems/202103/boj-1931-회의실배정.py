def solution(arr):
    answer = 0
    endTime = 0
    for i in range(len(arr)):
        if endTime <= arr[i][0]:
            endTime = arr[i][1]
            answer += 1
    return answer


N = int(input())
arr = []

for i in range(N):
    A, B = map(int, input().split())
    arr.append([A, B])

# 두가지 기준으로 정렬 => 끝나는 시간으로 먼저 오름차순 정렬한후 시작하는 시간으로 오름차순 정렬
# 이렇게 하면 끝나는 시간이 가장 빠른 예약 중 시작하는 시간이 가장 빠른 예약부터 순회하게 됨
# 그런 상태에서 가장 앞에 올 수 있는 것을 먼저 픽하면 자연스럽게 최대치로 우겨넣을 수 있게 됨

arr.sort(key=lambda x: (x[1], x[0]))
print(solution(arr))