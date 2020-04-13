# 백준 9461: 파도반 수열
# https://www.acmicpc.net/problem/9461
# 시간 : 15분
# 경과 : 맞았습니다(72ms)

data_num = int(input())

for _ in range(data_num):
    num = int(input())
    padovan = [1, 1, 1, 2, 2]
    if num < 6:
        print(padovan[num-1])
        continue
    for idx in range(num-5):
        new_num = padovan[-1] + padovan[idx]
        padovan.append(new_num)
    print(padovan[-1])

#! 접근) 이것도 일단 노가다로 규칙을 찾아내야 했음
#! 접근) kn = kn-1 + kn-5(n>6)이라는 점화식이 성립
