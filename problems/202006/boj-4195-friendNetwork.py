# 백준 4195번 친구 네트워크
# https://www.acmicpc.net/problem/4195
# 시간 : 1시간 - 못품
# 경과 : 못품
# * 나동빈 문제


def find(x):
    # 집합의 head 부모 리턴
    if x == parent[x]:
        return x
    # 해당 집합의 head를 지 집합으로 삼음
    else:
        # 재귀적으로 집합 헤드를 찾아냄
        p = find(parent[x])
        # ? 맨날 갱신해야됨? 갱신함
        #! 일단 헤드 집합 찾고 갱신해서 지가 어디에 속해있는지 정확히 알아야
        parent[x] = p
        return parent[x]


# 둘이 이어버림
def union(x, y):
    # 집합 정보를 받고
    x, y = find(x), find(y)
    # 다른 네트워크에 있으면 number 값을 더해줌 + 한쪽 집합을 다른쪽으로 갱신해줌
    if x != y:
        parent[y] = x
        number[x] += number[y]


test_case = int(input())
for _ in range(test_case):
    parent, number = dict(), dict()
    f = int(input())
    for _ in range(f):
        x, y = input().split(" ")
        # 없는사람이면 집합 만들어주기
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        # 둘이 이어서 네트워크 값을 리턴
        union(x, y)

        # x 네트워크의 크기를 리턴한다, 양쪽 중 하나만 해도 됨
        print(number[find(x)])

#! 유니언 파인드 자료구조를 이용한다
"""
원소들의 연결 여부, 네트워크의 크기를 확인할 수 있는 자료구조

1. 각 노드들은 처음에 각자 자기 자신을 부모로 삼는 포함한 각각의 집합에 포함됨, 그 집합의 원소는 1개
2. 그거를 리스트로 표현하면 최초에 [1,2,3,4] 인데, 다 각자 집합에 들어가있는 상황임
2. 노드들이 연결되기 시작하면 특정 노드가 다른 노드와 부모-자식 관계를 맺고, 부모 노드 집합의 원소는 1개보다 늘어남
3. 연결된 노드들은 모두 부모를 갖는데, a노드를 부모로 가진 b노드에 연결된 c는 a집합에 포함됨 : 재귀적으로 자기자신을 부모로 갖는 노드가 집합의 head 부모
4. 지 인덱스가 곧 지 집합인 얘가 집합의 head 부모. 거기까지 거슬러 올라가서 자기 집합으로 삼음
5. 만약에 리스트가 [1,1,3,1]이 되면 {1,2,4} 네트워크 하나, {3}네트워크 하나 이런거임 그러니깐..
"""
