# 백준 11054: 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054
# 시간 : 60분
# 경과 : 틀렸습니다 => 못품


n = int(input())
lst = list(map(int, input().split()))
dp_left = [1] * n
dp_right = [1] * n


# 왼쪽에서부터 최대증가수열 구하기
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            if dp_left[i] < dp_left[j] + 1:
                dp_left[i] = dp_left[j] + 1


# 오른쪽에서부터 최대 증가수열 구하기 range(시작점, -1, -1) : 첨부터끝까지 반대로
# 이때 인덱스 역시 거꾸로 넣어야 한다
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if lst[j] < lst[i]:
            if dp_right[i] < dp_right[j] + 1:
                dp_right[i] = dp_right[j] + 1

dp = [dp_left[i] + dp_right[i] for i in range(n)]

# 수열을 두번 구했으니 1이 두번 더해졌을 것이므로 하나는 뺀다
print(max(dp) - 1)

#! 쉽게 생각하면 됐었다, 어느 기점으로 증가, 어느기점으로 감소
#! 어느 기점으로 감소하는 수열을 구하기 위해서 자료형의 반대로 증가수열을 구해주는 방법으로다가
#! 자료형을 뒤집는 액션 옵션에 넣기
