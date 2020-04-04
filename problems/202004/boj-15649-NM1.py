# 백준 15649 : N과 M - 1
# https://www.acmicpc.net/problem/1436
# 시간 : 35분
# 경과 : 맞았습니다(188ms)


def DFS(num_list, result, size):
    if len(result) == size:
        print(" ".join(map(str, result)))
        return
    for num in num_list:
        current_result, current_num_list = result[:], num_list[:]
        current_result.append(num)
        current_num_list.remove(num)
        DFS(current_num_list, current_result, size)


N, M = map(int, input().split())
num_list = [n for n in range(1, N+1)]
DFS(num_list, [], M)

#! 모듈 사용 - 시간을 100ms 가까이 줄일 수 있음(itertools 모듈 한번 보기)
#! 문자열 + enumerate(더 깔끔한듯)
"""
def recur(arr, string, n):
    if n == 0:
        print(string)
        return

    for i, item in enumerate(arr):
        arr.pop(i)
        recur(arr, string + '{} '.format(item), n - 1)
        arr.insert(i, item)

recur([i for i in range(1, n + 1)], '', m)
"""
