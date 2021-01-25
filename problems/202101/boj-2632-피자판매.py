import sys

target = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
left = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
right = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

left_sum = [0]*2000001
left_sum[0] = 1
l_length, r_length = len(left), len(right)

left_sum[sum(left)] = 1

for i in range(l_length):
    s = 0
    for j in range(l_length):
        s += left[(i+j) % m]
        if s > target:
            break
        else:
            left_sum[s] += 1

ans = 0

for i in range(r_length):
    s = 0
    for j in range(r_length):
        s += right[(i+j) % n]
        if s > target:
            break
        else:
            if left_sum[target - s]:
                ans += (left_sum[s] * left_sum[target - s])

print(ans)
