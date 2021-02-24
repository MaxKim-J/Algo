def stars(n):
    # 구배열을 기준으로 새로운 배열 리턴
    matrix = []
    #! 결국 몇번을 어떤 단위로 뭐를 출력할지는 타진을 해봐야됨
    for i in range(3 * len(n)):
        # 3으로 나누어 떨어지는 경우일때 다른 패턴을 낸다
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))


# 배열에 계속 담아내는 느낌으로
star = ["***", "* *", "***"]

n = int(input())
k = 0

# 횟수를 이런식으로 먼저 구했음
while n != 3:
    n = int(n / 3)
    k += 1

# 횟수만큼 star을 채우기
# 재귀라기 보다는... 다 채워서 리턴하는 느낌쓰
for i in range(k):
    # 3일때의 배열을 계속 키워나간다
    star = stars(star)

for i in star:
    print(i)
