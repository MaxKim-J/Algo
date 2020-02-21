# 자력으로 풀었음 넘 좋음..

N = int(input())

def polygon(num):
    if num == 1:
        return 1
    key_num, plus = 1, 0
    while num > key_num:
        key_num += plus*6
        plus += 1
    return plus

print(polygon(N))