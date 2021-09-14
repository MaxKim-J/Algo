from math import inf # min이나 max칠때 limit을 못구하겠으면, 애매하면 그냥 Inf쓰자
# JS에서는 Infinity라는 객체가 있다

def solution(n, s, a, b, fares):
    answer = inf

    # 사실 그래프 이차원 배열은 하나만 있으면 된다
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