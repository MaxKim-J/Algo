from math import inf

def solution(n, s, a, b, fares):
    answer = inf
    dist = [[inf]*n for _ in range(n)]
    
    for fare in fares:
        c, d, f = fare
        dist[c-1][d-1] = dist[d-1][c-1] = f
    
    for i in range(n):
        dist[i][i] = 0
    
    for d in range(n):
        for r in range(n):
            for c in range(n):
                if dist[r][c] > dist[r][d] + dist[d][c]:
                    dist[r][c] = dist[r][d] + dist[d][c]
    
    for l in range(n):
        fee = dist[s-1][l] + dist[l][a-1] + dist[l][b-1]
        answer = min(answer, fee)
        
    return answer