# 재귀로 들어가던지 아니면 프린트를 하든지
#! "없으면 무시" 이거 잘 생각하면 순서 나옴


class Node:
    # 쉽게 연산하기 위해 노드 클래스 만들어주기
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    # 전위순회(나 -> 왼 -> 오)
    # * 직관적인 순서 => 탐색중에 일단 간곳은 출력하고봄
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    # 중위순회(왼 -> 나 -> 오)
    # * 왼쪽부터 출력하도록 만드는 순서가 됨
    # 재귀 스택이 시작되면 left가 리프까지 내려감
    if node.left_node != '.':
        in_order(tree[node.left_node])
    # 거기서부터 데이터 출력함
    print(node.data, end='')
    # 그리고 오른쪽 자식봄(없으면 무시)
    if node.right_node != '.':
        in_order(tree[node.right_node])


def post_order(node):
    # 후위순회(왼 -> 오 -> 나)
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')


n = int(input())
# 트리를 딕셔너리로 표현
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
