# 트리의 부모 찾기 백준 11725
import sys

node = int(input())
tree = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    tree[i].append(j)
    tree[j].append(i)


def dfs(tree_list, start, parent):
    visited = [start]
    while visited:
        node = visited.pop()
        for i in tree_list[node]:
            parent[i].append(node)
            visited.append(i)
            tree_list[i].remove(node)
    return parent


for i in list(dfs(tree, 1, parent))[2:]:
    print(i[0])
