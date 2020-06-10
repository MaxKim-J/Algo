# 백준 1568번 새
# https://www.acmicpc.net/problem/1568
# 시간 : 5분
# 경과 : 맞았습니다(72ms)
# * 나동빈 문제

birds = int(input())
count, sing = 1, 0

while birds > 0:
    if birds >= count:
        birds -= count
        sing += 1
        count += 1
    else:
        count = 1

print(sing)
