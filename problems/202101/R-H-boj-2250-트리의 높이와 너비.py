# 이거 딕셔너리로 대체가 가능할까?
# * 이렇게 하면 편하다는... 보장이 있어야 가능함


class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    #! 이게...이게 정말 실력의 결정체...
    global level_depth, x
    level_depth = max(level_depth, level)
    # 다음레벨로 중위순회 시작
    # 처음 재귀 쌓으면서 들어갈때 level을 증가시켜서 기록한다
    # * 왼쪽
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)
    # 입력 받으면서 레벨의 최소최대를 구할 수 있다
    # * 본인
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    # 얘는 너비 구할때 쓰이는 가로값, 중위순회에서 자신을 호출하는 순서에서 기록하고
    # 하나 올려줌(재귀 스택에서도 기록한 후 올림)
    x += 1
    # * 오른쪽
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, n+1):
    # 초기화
    tree[i] = Node(i, -1, -1)
    # 각 레벨의 최소와 최대값 정리한 배열, 인덱스로 접근
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    # 이어주기, 트리에 정보 채우기
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    # 부모 연결
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

for i in range(1, n+1):
    # 루트 찾기
    if tree[i].parent == -1:
        root = i

# 루트부터 중위순회, 중위순회하면서 데이터 확보
in_order(tree[root], 1)

# 최대레벨과 최대레벨의 너비 구하기
result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)
