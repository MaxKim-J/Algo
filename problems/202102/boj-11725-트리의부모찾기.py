'''
DFS가 더 빠름 => 더 많은 노드를 한번에 제낄 수 있기 때문에
전체 순회 성능은 어쩔지 몰라도, 중요한 것은 부모 관계를 더 빨리 규명하는 것임
어떤 방법이 더 가지치기가 빡세게 되느냐
'''

# 젤 빨랐던 풀이(Python3에서 돌아감)

N = int(input())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

result = [-1, -1] + [0] * (N-1)


def DFS():
    stack = [1]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            result[i] = node
            stack.append(i)
            # 사실 어쩌면 순회하는 자료형 바로 없애서 백트랙킹 하는게 직빵일지도
            graph[i].remove(node)


DFS()

for i in range(2, N+1):
    print(result[i])


'''
pypy3에서 돌아간 풀이

N = int(input())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

result = [-1, -1] + [0] * (N-1)


def DFS():
    stack = [1]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if result[i] == 0:
                result[i] = node
                stack.append(i)


DFS()

for i in range(2, N+1):
    print(result[i])
'''
