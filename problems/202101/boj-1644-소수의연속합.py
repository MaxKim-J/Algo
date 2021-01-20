# 투포인터 + 에라토스테네스
# 가끔 이런 원플원 짬뽕문제가 하나씩 나옴


def prime_number_list(num):
    # 에라토스테네스의 체
    result = [True] * (num + 1)
    limit = int(num ** 0.5) + 1
    for i in range(2, limit):
        if result[i]:
            for j in range(i+i, num + 1, i):
                result[j] = False
    return [i for i in range(2, num + 1) if result[i] != False]


N = int(input())
prime_numbers = prime_number_list(N)
start = end = total = count = 0

# 좀더 정확히 이해할 필요가 있음
while True:
    if total >= N:
        if total == N:
            count += 1
        total -= prime_numbers[start]
        start += 1
    elif end == len(prime_numbers):
        break
    else:
        total += prime_numbers[end]
        end += 1

print(count)
