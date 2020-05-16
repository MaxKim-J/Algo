# 백준 5086: 배수와 약수
# https://www.acmicpc.net/problem/5086
# 시간 : 10분
# 경과 : 맞았습니다(60ms)


while True:
    num = list(map(int, input().split()))
    if num == [0, 0]:
        break
    if (num[0] < num[1]) and (num[1] % num[0] == 0):
        print("factor")
    elif (num[0] > num[1]) and (num[0] % num[1] == 0):
        print("multiple")
    else:
        print("neither")
