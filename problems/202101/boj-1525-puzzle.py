# 최단 접근은 BFS가 좋다 => 같은 depth에 있는 노드들을 쳐다보기 때문에, 조건을 만족하면 거기까지만 하면 된다
# 물론 그 경우의 수 자체를 큐에 넣어야 하니 메모리를 많이 쓰게 된다는 단점은 있다
# 방문했던 순간이 항상 최단이므로 방문했던 곳을 무시할 수 있다
# 메모리 적게 사용하는게 중요하니까 이차원 배열을 문자열로 바꾸어서 사용하면 좋다
# 접근은 비슷했는데....메모리도 그렇고 좀 타이핑이 긴게 많아서 보기도 힘들었고, 자료구조를 좀 낭비한거 같다(특히 배열 남발한거 같음)

import sys

dcol = [-1, 0, 1, 0]
drow = [0, -1, 0, 1]


def swap(s, n, k):
    i = s[n]
    m = s[k]
    s = s[:k] + i + s[k+1:]
    s = s[:n] + m + s[n+1:]
    return s


def is_range(row, col):
    if col >= 3 or col < 0:
        return False
    if row >= 3 or row < 0:
        return False
    return True


def bfs(puzzle_string):
    result = -1
    queue = []
    queue.append((puzzle_string, 0))
    # 아예 문자열 전체를 하나의 노드로 보는 방법
    #! 어떤걸 그래프를 식별할 수 있는 값으로 볼것인가가 중요하다. 탐색문제에서 벗어나지 않는 것은 경우의 수라고 생각하면 좋을듯?
    visit[puzzle_string] = 1
    while queue:
        puzzle_current, time = queue.pop(0)
        if puzzle_current == target:
            result = time
            break
        # 이차원을 선형으로 바꾸는 작업임
        # 1차원으로 바꾸면 0을 찾아내기 굉장히 쉬워진다(...)
        pos = puzzle_current.find('0')
        row = pos // 3
        col = pos % 3
        # 이런 태크닉도 괜찮은거 같다
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if is_range(nrow, ncol) is False:
                continue
            puzzle_new = puzzle_current
            # 0의 위치를 옮긴다
            puzzle_new = swap(puzzle_new, pos, nrow*3 + ncol)
            if not visit.get(puzzle_new):
                visit[puzzle_new] = 1
                queue.append((puzzle_new, time + 1))
    return result


puzzle = ''
visit = dict()
for i in range(3):
    line = []
    line = list(map(int, sys.stdin.readline().split()))
    puzzle += str(line[0]) + str(line[1]) + str(line[2])
target = '123456780'
result = 0
result = bfs(puzzle)
print(result)


# import copy

# puzzle = []
# initX, initY = 0, 0
# target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# for _ in range(3):
#     puzzle.append(list(map(int, input().split())))

# for i in range(3):
#     for j in range(3):
#         if puzzle[i][j] == 0:
#             initX = i
#             initY = j

# queue = []
# visited = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# queue.append([(initX, initY), 0, puzzle])


# def enable_node(x, y):
#     result = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
#     return list(filter(lambda x: (-1 < x[0] < 3) and (-1 < x[1] < 3), result))


# while True:
#     visit = queue.pop(0)
#     current_x = visit[0][0]
#     current_y = visit[0][1]
#     depth = visit[1]
#     visited[current_x][current_y] = 1
#     for (x, y) in enable_node(current_x, current_y):
#         if visited[x][y] != 1:
#             new_puzzle = copy.deepcopy(visit[2])
#             new_puzzle[x][y], new_puzzle[current_x][current_y] = new_puzzle[current_x][current_y], new_puzzle[x][y]
#             queue.append([(x, y), depth + 1, new_puzzle])
#     if visit[2] == target:
#         print(depth)
#         break
#     if len(queue) == 0:
#         print(-1)
#         break
