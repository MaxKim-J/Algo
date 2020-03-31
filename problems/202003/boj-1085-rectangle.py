# 백준 1085 : 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085
# 시간 : 5분 
# 경과 : 맞았습니다 


x, y, w, h = map(int, input().split())

dist = [h-y, y, x, w-x]
print(min(dist))