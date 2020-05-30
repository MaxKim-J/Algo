# 백준 1966: 프린터 큐
# https://www.acmicpc.net/problem/1966
# 시간 : 28분
# 경과 : 맞았습니다(108ms)
#! 동빈나 수업 문제

test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
