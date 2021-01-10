'''
백준 3108 <로고>

손도못댐 : 아무리 생각해도 최적해에 가까운 방법을 찾지 못할거같음
생각해본 것 : 선분과의 접점을 찾아내서 유니언파인드 하는 방법으로 접근함
풀이 찾아서 정리 : 
  - 복잡해보이지만 한붓그리기 문제이다
  - 예제 입력처럼 접점이 없는 사각형이 있지만 좌표상으로는 한칸차이라서 bfs로 바로 이동 가능한 케이스 존재
  - 사각형의 모든 길이를 2배

보니깐 유니언 파인드랑 BFS 두방법으로 모두 풀 수 있는 것 같다
이 기회에 유니언 파인드를 머리에 넣자
'''

import sys
# 오;
input = sys.stdin.readline

# 이거 외우자
# 파인드는 parent 딕셔너리의 가장 최상위 집합을 찾아가고 재귀로 구현


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

# 유니언은 파인드를 한 집합을 합치는 역할을 함


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
    return


N = int(input())
# 사각형 번호 찾기. 번호로 인덱싱이 가능하기때문에 걍 배열을 썼다 딕셔너리 써도 됨
parent = [i for i in range(N+1)]

# visited 딕셔너리는 평가한 좌표가 어떤 사각형 집합에 속하는지 기록한다
# * 점: 사각형 => 이런식으로 사각형을 이루는 모든 좌표가 집합을 가진다
# * 좌표가 -500<x<500 이므로 최대 4000개의 좌표가 들어가고
# * 사각형이 최대 천개이므로 4000 * 1000 = 4000000 => 1초안에 쌉가능이다;;
visited = {}

for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    # 점을 받아서 range로 순회하면 바로 선분의 범위에 접근할 수 있다
    # 사각형을 이루는 좌표를 모두 딕셔너리에다가 넣는다

    # 세로 두 선분
    # 사각형을 이루는 y의 모든 범위 순회 -> x 두값과 매치
    for j in range(y1+1, y2):
        # x1, x2를 x좌표로 가진 점에 이미 방문했다면 어떤 사각형에 이미 포함되어있는 점이다
        # 이것은 어떤 사각형과 다른 사각형은 한붓그리기가 가능하다는 말이 된다
        # 따라서 이번 순회하는 사각형의 집합과 유니언한다.
        if visited.get((x1, j)):
            union(i, visited.get((x1, j)))
        if visited.get((x2, j)):
            union(i, visited.get((x2, j)))
        # 이 점이 어떤 사각형에 포함되어있는지 기록한다
        visited[(x1, j)] = i
        visited[(x2, j)] = i

    # 가로 두 선분
    # 사각형을 이루는 x의 모든 범위 순회 -> y의 두 값과 매치
    for j in range(x1, x2+1):
        if visited.get((j, y1)):
            union(i, visited.get((j, y1)))
        if visited.get((j, y2)):
            union(i, visited.get((j, y2)))
        visited[(j, y1)] = i
        visited[(j, y2)] = i

# 0,0에 사각형이 걸쳐있을 경우 펜다운한 상태이므로 바로 사각형을 그리기 시작할 수 있다 그래서 -1로 초기화
# 사각형이 걸쳐있지 않을 경우 펜업을 한번 해서 이동해야한다
ans = -1 if visited.get((0, 0)) else 0

# 집합의 개수가 곧 답이 된다
for i in range(1, N+1):
    if parent[i] == i:
        ans += 1

print(ans)
