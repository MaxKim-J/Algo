# 백준 1463: 1로 만들기
# https://www.acmicpc.net/problem/1463
# 시간 : 28분
# 경과 : 맞았습니다(96ms)


num = int(input())
count, dp = 0, [num]

while (1 not in dp):
    temp = []
    for n in dp:
        if (n % 3 == 0) and (n//3 not in dp):
            temp.append(n // 3)
        if (n % 2 == 0) and (n//2 not in dp):
            temp.append(n // 2)
        if ((n-1) not in dp):
            temp.append(n-1)
    count += 1
    dp = temp[:]
print(count)

"""
# 특이한 풀이(56ms)

save = {1:0, 2:1}

# 분할정복, 이건 퇴각검색에 더 가까움
def frog(n):
    # 딕셔너리에 넣어놓고 수가 줄어들때까지 계속 진행
    if n in save:
        return save[n]
    m = 1+min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))
"""
