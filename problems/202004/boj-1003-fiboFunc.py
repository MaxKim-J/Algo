# 백준 1003 : 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 시간 : 14분
# 경과 : 맞았습니다(80ms)


N = int(input())

for _ in range(N):
    num = int(input())
    zero, one = [1, 0], [0, 1]
    if num < 2:
        print(zero[num], one[num])
        continue
    for i in range(num-1):
        zero.append(zero[i] + zero[i+1])
        one.append(one[i] + one[i+1])
    print(zero[-1], one[-1])

# ? zip이나 튜플 리스트로 더 간단하게 푸는 방법이 있을 것 같다
