# 백준 1543번 문서 찾기
# https://www.acmicpc.net/problem/1543
# 시간 : 15분
# 경과 : 맞았습니다(60ms)
# * 나동빈 문제

target = input()
find = input()

find_length, target_length = len(find), len(target)
idx = 0
count = 0

while idx < target_length:
    if find == target[idx:idx+find_length]:
        count += 1
        idx += find_length
    else:
        idx += 1

print(count)

#! 최대 문자열 길이 2500, 비교 문자열 길이 50 => 전체 탐색해서 풀 수 있어야 함
#! 겹치면 안됨 => 탐색하되 일치하면 length만큼 인덱스 증가, 일치 안하면 1씩 증가
