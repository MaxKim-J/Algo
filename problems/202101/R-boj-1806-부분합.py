import sys

# 못품. 아직도 연속 부분합 이해 부족함
# 근데 넘 간단하네...계속 보면서 익히자

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 두 포인터 어디서부터 시작할지 잘 정하시긔
left = right = total = cnt = 0

# 이 둘이 구분된다. n이면 어쨋든 다더했을때 이상일수 잇음
result = n
flag = False

while True:
    # 합 이상을 아예 만들수가 없으면 여기 조건문을 넘어오지를 못함
    if total >= s:
        flag = True
        result = min(result, cnt)
        total -= arr[left]
        left += 1
        cnt -= 1
    elif right == n:
        break
    else:
        total += arr[right]
        right += 1
        # 얘도 처음부터 시작해도 됨
        cnt += 1

if flag:
    print(result)
else:
    print(0)
