# 백준 156650: N과 M - 4
# https://www.acmicpc.net/problem/15652
# 시간 : 10분
# 경과 : 맞았습니다(68ms)


def DFS(num_list, result, count):
    if count == 0:
        print(result)
        return
    for idx, num in enumerate(num_list):
        DFS(num_list[idx:], result + f"{str(num)} ", count - 1)


N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
DFS(num_list, "", M)

#! 접근 1) itertools의 product메서드로 풀려고 했으나 잘 안됨
# * product메소드는 정말 모든 경우의 수를 구하는데는 강점을 가지지만, 필터링 하는건 또 다른 일이라서
# * 프로덕트 메소드에 필터링이 용이하게 인자를 넘기지 못하면 적용하기가 힘들 것 같음
# * 모든 조건 = 프로덕트, 필터링 = 제고
# ? 근데 2번도 그랬는데 필터링 조건이 들어가야하는 문제들은 itertools없이 풀어도 시간이 비슷함(결국 후처리가 필요하다는 것)
