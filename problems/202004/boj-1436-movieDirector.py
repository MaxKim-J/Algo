# 백준 1436 영화감독 숌
# https://www.acmicpc.net/problem/1436
# 시간 : 15분
# 경과 : 맞았습니다(832ms)

N = int(input())

num, count = 665, 0
while count < N:
    num += 1
    if "666" in str(num):
        count += 1
print(num)

# ? 시간을 확 줄일 수 있는 방법이 있을까 싶은데 잘 모르겠다.. 체점 기록에는 600ms짜리도 있는데 어캐한걸까
# ? 진짜 첨부터 끝까지 나올때가지 순회하는게 필요한걸까
# * 정규표현식을 쓰면 더느려진다 (1726ms)
