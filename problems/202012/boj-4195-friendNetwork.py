def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
        # 집합을 대표하는 값의 number만 찾아주면 됨
        # 다른 넘버는 크게 필요없음
        number[x] += number[y]


test_case = int(input())
for _ in range(test_case):
    parent, number = dict(), dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(" ")
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)

        print(number[find(x)])

'''
그래프를 구성하는 노드의 개수 리턴
유니언 파인드 알고리즘 이용하기(합집합)
전체 자료구조를 일단 다 구현할 필요가 없음 목적 지향적으로 생각하기

유니언 파인드:
1. 맨 처음에 자기 자신으로 네트워크 구성(각자 식별자)
2. 노드들이 관계를 맺으면서 식별자를 수정함
3. 식별자 종류의 수만큼 그룹이 만들어짐

디바이드 앤 컨쿼:
1. find => 타고 올라가서 부모를 찾아가는 함수, 부모를 타고 올라가서 
2. union => 부모를 합쳐서 연결
3. parent라는 배열을 만들어서 식별자를 동기화함
4. 부모테이블에서 한 노드는 하나만 가리키고 있으면 됨, 초기에는 자신을 가리키고 있다가
'''
