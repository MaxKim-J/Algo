# 객체들의 네트워크, 연결여부를 구하는 알고리즘

# 집합이 주어졌을 때 재귀적으로 가장 상위의 집합 번호를 구함
# 지가 곧 지 집합의 번호인 것이 가장 상위 집합
def find(x):
    while parent[x] != x:
        x = find(parent[x])
    return x


# 두 집합을 합치면서 상/하위관계를 정의
def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x

# 어떤 집합에 종속적인지 == parent
# 집합의 크기 표현 == number
parent = []

# 관계의 개수
r = int(input())

for _ in range(r):
    # 관계들
    x, y = input().split(" ")
    if x not in parent:
        parent[x] = x
    if y not in parent:
        parent[y] = y

    union(x, y)

    print(parent)