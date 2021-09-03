# 메모이제이션과 BFS를 이용한다
# DFS로 하면 너무 해매고(시간초과남), DP로 하기에는 코너 도는 정보 확인이 불가능하다

from collections import deque

dr = (-1,0,1,0)
dc = (0,1,0,-1)

def solution(board):

    def BFS(init):
        queue = deque(init)
        # visited를 분리하는 것 까진 괜찮다(이차원 배열 두개 만들기)
        check = [[0 for _ in range(n)] for _ in range(n)]
        check[init[0][0]][init[0][1]] = 100
        
        while queue:
            r,c,cost,d = queue.popleft()
            if (r == n-1) and (c == n-1): # 도달 했다 하면 일단 끊어줘야한다(다시 거기서 딴데갓다가 값이 낮아져서 다시 갱신될수도 있음)
                answer.append(cost)
                continue
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if (-1<nr<n) and (-1<nc<n):
                    new_dir = d
                    new_fee = cost + 100
                    
                    # 숫자로 방향값 전부를 표현하는게 더 낫다(Hor과 ver도)
                    if d == 'hor' and (i % 2 == 0):
                        new_dir = 'ver'
                        new_fee += 500
                        
                    if d == 'ver' and (i % 2 != 0):
                        new_dir = 'hor'
                        new_fee += 500
                    
                    if not board[nr][nc]:
                        if not check[nr][nc] or check[nr][nc] > new_fee:
                            check[nr][nc] = new_fee
                            queue.append((nr, nc, new_fee, new_dir))
                            # 큐에 넣는건 처음에는 최대한 넉넉히 생각하는게 좋은거같다
                            # 나중에 필요없을때 빼면 되구
                            
    answer = []
    n = len(board[0])
    board[0][0] = 1
    
    # 두개를 나눠서 돌려준다
    # 같이 돌리면 너무 방해된다 => 두개의 방향을 계속 살려서 돌려야 하는데
    if(board[0][1] != 1):
        BFS([(0,1,100,'hor')]) # 이미 한칸은 갔다는 전제니까 100도 같이 넣어주기
        
    if(board[1][0] != 1):
        BFS([(1,0,100,'ver')])
    
    # answer배열에 들어가는건 꼭 check[n-1][n-1] 값 뿐만은 아니다
    # 시작점부터 끝까지 해서 도착점까지 찍은 모든 값들이 들어간다
    return min(answer)