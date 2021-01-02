def recursion(current, new):
    global count, n
    current += new
    if current > n:
        return
    elif current == n:
        count += 1
        return
    else:
        recursion(current, 1)
        recursion(current, 2)
        recursion(current, 3)


N = int(input())

for _ in range(N):
    count = 0
    n = int(input())
    recursion(0, 1)
    recursion(0, 2)
    recursion(0, 3)
    print(count)

# 20분
# DP로 풀수있는 방법을 시간이 나면 고민해봐야할 것
# 처음에 연산을 유추하는 습관 => 완전탐색은 비용이 크므로
