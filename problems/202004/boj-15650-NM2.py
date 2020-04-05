# 백준 156650: N과 M - 2
# https://www.acmicpc.net/problem/15650
# 시간 : 40분
# 경과 : 맞았습니다(56ms)


def DFS(num_list, result, count):
    if count == 0:
        print(result)
        return

    for idx, num in enumerate(num_list):
        current_result = result
        current_result += f"{str(num)} "
        current_num_list = num_list[idx:]
        current_num_list.pop(0)
        DFS(current_num_list, current_result, count - 1)


N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
DFS(num_list, "", M)

#! 중점1 ) 값을 그대로 가져가는게 아니라 복사하는게 중요하다
# * 왜? 재귀로 부를때마다 다른 result가 필요하기 때문이라고 생각하면 편할듯?
