E, S, M = map(int, input().split(' '))
count = 0

while True:
    E -= 1
    S -= 1
    M -= 1
    count += 1
    if E == 0 and S == 0 and M == 0:
        break
    if E == 0:
        E = 15
    if S == 0:
        S = 28
    if M == 0:
        M = 19

print(count)

# 13분
# 이것 역시 숫자가 그렇게 크지 않다 => 완전탐색으로 가능함
# 그냥 무식하게 빼버리기~
