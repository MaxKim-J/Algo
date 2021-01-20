# 요런 문제유형에 익숙하지 못한듯...
# 중복되는 덧셈연산을 최소화

#! 스르륵 훑을 수 있는 방법 생각하기
#! 모든 연속수열의 경우를 다 구하는건 아님(백트랙킹) => 그래도 답찾기는 가능
#! 이미 더한 것중에서 하나 빼고, 새로운 값을 더하고 반복하면서 값 찾기

N, M = map(int, input().split())
order = list(map(int, input().split()))
count = 0
start, end = 0, 1
sum_value = order[start]  # 연속합 저장

while start < N:
    # 찾는값 미만이면 다음 숫자 더함
    if sum_value < M:
        # 더 더할수가 없음
        if end == N:
            break
        sum_value += order[end]
        end += 1
    # 찾는값 이상이면 뒤에서 하나뺌
    elif sum_value >= M:
        # 찾음
        if sum_value == M:
            count += 1
        sum_value -= order[start]
        start += 1

print(count)
