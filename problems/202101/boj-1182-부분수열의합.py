import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0


def subSet(idx, total):
    global ans

    if idx >= n:
        return
    total += num_list[idx]
    if total == s:
        ans += 1
    # 부분수열을 만드는 두가지 경우의 수, 현재 값을 뺀 다음값부터 포함시킴
    subSet(idx + 1, total - num_list[idx])
    # 현재 값을 포함시켜 다음값을 찾음
    subSet(idx + 1, total)


subSet(0, 0)
print(ans)
