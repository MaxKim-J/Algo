# 백준 15651: N과 M - 2=3
# https://www.acmicpc.net/problem/15651
# 시간 : 4분
# 경과 : 맞았습니다(868ms)


def DFS(num_list, result, count):
    if count == 0:
        print(result)
        return
    for num in num_list:
        DFS(num_list[:], result + f"{str(num)} ", count - 1)


N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
DFS(num_list, "", M)
