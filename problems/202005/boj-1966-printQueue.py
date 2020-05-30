# 백준 1966: 프린터 큐
# https://www.acmicpc.net/problem/1966
# 시간 : 28분
# 경과 : 맞았습니다(108ms)
#! 동빈나 수업 문제

test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    # enumertate로 인덱스를 같이 쓰는거
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0

    # break를 중첩하는게 그리 좋은 방식은 아닌거 같다
    while True:
        # max함수에 두번째 인자로 비교할 값을 지정해줄 수 있다
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

#! 문제를 무시하지 말자 죽기살기로 풀기..
