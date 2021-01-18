N, M = map(int, input().split())
trees = list(map(int, input().split()))

#! 1: 이분탐색의 진입조건 : 최소와 최대
start = 0
end = max(trees)
result = start

#! 2: 최소랑 최대를 계속 갱신해가면서 적정값을 찾는
# 1, 10 => 5
# 6, 10 => 8
# 9, 10 => 9
# 10, 10 => 10
# 10, 9 => 끝
# * 이분탐색이 끝나는 경우의수 => 정해져있음 => 다음시간에 정리해서

while start <= end:
    mid = (start + end) // 2
    total_log = 0
    for tree in trees:
        total_log += max(tree - mid, 0)
    # "적어도 M미터의 나무를 집에 가겨지기 위한 절단기 높이의 최대값"
    #! 3: 이분탐색의 마지막 결과값을 찾을때 start값을 마지막으로 갱신하는 값을 저장
    if total_log <= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
