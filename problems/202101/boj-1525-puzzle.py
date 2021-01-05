import copy

puzzle = []
initX, initY = 0, 0
target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

for _ in range(3):
    puzzle.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        if puzzle[i][j] == 0:
            initX = i
            initY = j

queue = []
visited = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
queue.append([(initX, initY), 0, puzzle])


def enable_node(x, y):
    result = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    return list(filter(lambda x: (-1 < x[0] < 3) and (-1 < x[1] < 3), result))


while True:
    visit = queue.pop(0)
    current_x = visit[0][0]
    current_y = visit[0][1]
    depth = visit[1]
    visited[current_x][current_y] = 1
    for (x, y) in enable_node(current_x, current_y):
        if visited[x][y] != 1:
            new_puzzle = copy.deepcopy(visit[2])
            new_puzzle[x][y], new_puzzle[current_x][current_y] = new_puzzle[current_x][current_y], new_puzzle[x][y]
            queue.append([(x, y), depth + 1, new_puzzle])
    if visit[2] == target:
        print(depth)
        break
    if len(queue) == 0:
        print(-1)
        break
