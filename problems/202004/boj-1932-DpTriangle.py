# 백준 1932: 정수 삼각형
# https://www.acmicpc.net/problem/1932
# 시간 : 16분
# 경과 : 맞았습니다(152ms)


from sys import stdin

N = int(stdin.readline())
tri = [list(map(int, stdin.readline().split())) for _ in range(N)]

for i in range(N-1, 0, -1):
    for j in range(i):
        tri[i-1][j] += max(tri[i][j], tri[i][j+1])
print(tri[0][0])

# * 접근 :  삼각형 밑부터 위로 인접한 최대값을 계속 더하면 됨
