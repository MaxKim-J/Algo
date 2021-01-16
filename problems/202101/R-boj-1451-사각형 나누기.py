# 못품
# 주어진 사각형에서 3그룹으로 나눌 수 있는 모든 조건에 대해서만 검사를 수행 => 그렇지 못하면 시간초과
# 가능한 방법의 수는 6가지로 똑 떨어진다. 여섯번 이중포문을 돌린다
#! 이런 문제는 무조건 규칙이 있어야만 풀 수 있으니 먼저 규칙을 찾자
# ? 다음에 다시한번 보기,,

import sys

# 가로줄 수 * 세로줄 수
n, m = map(int, sys.stdin.readline().split())
# 입력이 꽤 클수도 있으므로 리드라인 사용하자
table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans = 0

# |||
# 막 순회해서 생각하지말고 직관적으로 사각형을 그리고있다고 생각할 것
# for문 두개는 그 범위를 잡아주는 역할을 한다.

# i는 시작점, J는 그 다음 시작점을 잡아준다 => 어짜피 직사각형이 3개니까 시작점 두개잡으면 하나는 쉽게 구할 수 있는듯
# 어떤 부분이 우선적으로 나눠질지 위에서 아래로 생각하면 답나온다
for i in range(1, m-1):
    for j in range(i+1, m):
        # 가로로 하나씩 줄어드니까 b가 그 다음행으로 간다
        # a는 무조건 가로줄 수 전체를 순회해야하므로 (0,n)임
        s1 = sum([table[a][b] for a in range(0, n) for b in range(0, i)])
        s2 = sum([table[a][b] for a in range(0, n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(0, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# ||
# --
for i in range(1, m):
    for j in range(1, n):
        # 가로줄 전체 혹은 일부를 순회해야하는 새로 바들의 a, 그리고 분할하는 b는 i 기준으로 앞 뒤
        s1 = sum([table[a][b] for a in range(0, j) for b in range(0, i)])
        s2 = sum([table[a][b] for a in range(0, j) for b in range(i, m)])
        # 새로 바들이 끝난 곳을 기준으로 나머지 가로줄을 순회하고, 모든 세로줄의 칸을 커버해야 하므로 0,m
        s3 = sum([table[a][b] for a in range(j, n) for b in range(0, m)])
        ans = max(ans, s1*s2*s3)

# --
# ||
# 순서가 상관이 있나? 아마 없을듯
for i in range(1, n):
    for j in range(1, m):
        # 먼저 가로로 분할 , 이때 M 전체 커버
        s1 = sum([table[a][b] for a in range(0, i) for b in range(0, m)])
        # 가로줄 위의 첫번째 사각형이 끝난 부분부터 세로로 분할
        s2 = sum([table[a][b] for a in range(i, n) for b in range(0, j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# =|
for i in range(1, n):
    for j in range(1, m):
        # 먼저 가로로 분할 , 이때 j까지 커버
        s1 = sum([table[a][b] for a in range(0, i) for b in range(0, j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(0, j)])
        # 남은 부분 세로로 분할 세로 전체 커버
        s3 = sum([table[a][b] for a in range(0, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# |=
for i in range(1, n):
    for j in range(1, m):
        # 가로분할
        s1 = sum([table[a][b] for a in range(0, i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        # 세로분할
        s3 = sum([table[a][b] for a in range(0, n) for b in range(0, j)])
        ans = max(ans, s1*s2*s3)

# -
# -
# -
for i in range(1, n-1):
    for j in range(i+1, n):
        # 가로 싹다커버
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)

print(ans)
