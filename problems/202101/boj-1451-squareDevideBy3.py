# 못품
# 주어진 사각형에서 3그룹으로 나눌 수 있는 모든 조건에 대해서만 검사를 수행 => 그렇지 못하면 시간초과
# 가능한 방법의 수는 6가지로 똑 떨어진다. 여섯번 이중포문을 돌린다

import sys

# 가로줄 수 * 세로줄 수
n, m = map(int, sys.stdin.readline().split())
# 입력이 꽤 클수도 있으므로 리드라인 사용하자
table = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans = 0

# |||
# 막 순회해서 생각하지말고 직관적으로 사각형을 그리고있다고 생각할 것
# for문 두개는 그 범위를 잡아주는 역할을 한다.

# i는 시작점
for i in range(1, m-1):
    for j in range(i+1, m):
        # 가로로 하나씩 줄어드니까 b가 그 다음행으로 간다
        s1 = sum([table[a][b] for a in range(n) for b in range(i)])
        s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# ||
# --
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)

# --
# ||
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# =|
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        ans = max(ans, s1*s2*s3)

# |=
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j)])
        ans = max(ans, s1*s2*s3)

# -
# -
# -
for i in range(1, n-1):
    for j in range(i+1, n):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        ans = max(ans, s1*s2*s3)

print(ans)
