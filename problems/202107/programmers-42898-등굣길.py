# 그러모으는 DFS
#! 시작점에서 목적지까지 갈 수 있는 경로를 시작점에 저장!
# 확실히 이해가 되는 느낌이네여

dr = [0, 1]
dc = [1, 0]

def solution(M,N,P):
    visited = [[-1 for j in range(M)] for i in range(N)]
    
    for pr, pc in P:
        visited[pc-1][pr-1] = -2 #! 문제 조건에서 r,c를 반대로 표현했다 (x,y) 좌표평면식이 (r,c)와 반대로라는 것을...명심하자

    def DFS(r, c, visited):
        if (r == N - 1) and (c == M - 1):
            return 1

        if (visited[r][c] != -1) and (visited[r][c] != -2):
            return visited[r][c]

        visited[r][c] = 0

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if (-1 < nr < N) and (-1 < nc < M) and (visited[nr][nc] != -2):
                visited[r][c] += DFS(nr, nc, visited)

        return visited[r][c] # 최후의 리턴값...

    answer = DFS(0,0,visited)
    
    return answer % 1000000007 #! 이걸 또 놓쳣음;;; 근데 이상한게 효율성에서만 에러남