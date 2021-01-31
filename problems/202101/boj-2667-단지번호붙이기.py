c_row = [0, 0, 1, -1]
c_col = [1, -1, 0, 0]


def DFS(row, col):
    global count, board, visited, N
    for i in range(4):
        n_row = row + c_row[i]
        n_col = col + c_col[i]
        if (0 <= n_row < N and 0 <= n_col < N) and (visited[n_row][n_col] == False):
            visited[n_row][n_col] = True
            if board[n_row][n_col] == '1':
                count += 1
                DFS(n_row, n_col)


N = int(input())
# N = 7
board = [list(input()) for _ in range(N)]
# board = [
#     ['0', '1', '1', '0', '1', '0', '0'],
#     ['0', '1', '1', '0', '1', '0', '1'], 
#     ['1', '1', '1', '0', '1', '0', '1'],
#     ['0', '0', '0', '0', '1', '1', '1'],
#     ['0', '1', '0', '0', '0', '0', '0'],
#     ['0', '1', '1', '1', '1', '1', '0'],
#     ['0', '1', '1', '1', '0', '0', '0'],
# ]
visited = [[False]*N for _ in range(N)]
result = []

for r in range(N):
    for c in range(N):
        if (visited[r][c] == False) and (board[r][c] == '1'):
            count = 1
            visited[r][c] = True
            DFS(r, c)
            if count != 0:
                result.append(count)

print(len(result))
for i in sorted(result):
    print(i)

# 처음 접근은 잘했는데 DFS의 visited여부를 헷갈리면서 시간이 좀 늘어났다. 소신을 가지고 풀자....!
# 꼼꼼하게 풀자!!! 작은거 하나라도 없으면 틀렸습니다 나옴... 스켈레톤 정리 잘하기
