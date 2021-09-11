'''
맞춤. 2시간 걸림

1. 문제가 너무 더럽다ㅋㅋㅋㅋ이쁜 BFS 불가능
2. 접근 자체는 잘 맞았는데 이차원 배열을 큐에 넘기고싶지 않아서 발악하느라 정답에서 자꾸 멀어졌던 것 같다
3. 두 카드 짝을 매칭시킬때 카드에 엔터를 눌렀다면 그 상황을 이차원 배열에 반영시켜야했다(0으로 만든다거나)
4. 짝이 다른 두개의 카드를 굳이 확인하는 동작은 배제하고 문제를 풀었는데 맞았다
5. 다른 사람 풀이 보니까 이차원 배열을 문자열로 바꿔서 풀기도 했고 visited를 set으로 이용한 사람도 있었다(딕셔너리의 값이 어짜피 1인 경우에는 이쪽도 괜찮겠다)
6. 딕셔너리나 집합에 불변하지 않은 것을 넘기지를 못하기 때문에 애초에 board를 넘겨야 한다면 조금 정리해서 넣는게 좋았겠다
7. 백트랙킹이 가능하고 그렇게 해야한다라는 생각을 계속 유지했던게 괜찮았던 것 같다
8. 근데 시간초과 뜰가봐 4*4배열이었음에도 자신있게 이차원 배열을 큐에 못집어넣었다..빨리빨리 생각을 전환해야 한다.
'''

from collections import deque
from copy import deepcopy

def is_end(board):
    result = 0
    for i in range(4):
        result += sum(board[i])
    return result == 0

def solution(board, r, c):
    dr = (1,0,-1,0)
    dc = (0,1,0,-1)
    
    card_count = 0
    
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                card_count += 1
    
    card_count //= 2
    
    visited={}
    queue=deque([((r,c),-1,deepcopy(board),0)])
    
    def update_queue(obj):
        if visited.get(str(obj)) == None:
            queue.append(obj)
            visited[str(obj)] = 1

    while queue:
        cur, pick, bo, depth = queue.popleft()
        cr, cc = cur
        
        if is_end(bo):
            return depth
        
        if bo[cr][cc] > 0:
            new_board = deepcopy(bo)
            if pick == -1: 
                new_board[cr][cc] = 0
                update_queue((cur, bo[cr][cc], new_board, depth+1))
            elif pick > 0:
                if (bo[cr][cc] == pick):
                    new_board[cr][cc] = 0
                    update_queue((cur, -1, new_board, depth+1))
                
        for i in range(4):
            # 그냥 방향키 이동
            nr = cr + dr[i]
            nc = cc + dc[i]
            if (-1 < nr < 4) and (-1 < nc < 4):
                update_queue(((nr,nc), pick, deepcopy(bo), depth+1))
            
            # ctrl 이동
            memo=None
            card_update_flag=False
            for j in range(1, 4):
                nr = cr + (dr[i] * j)
                nc = cc + (dc[i] * j)
                if (-1 < nr < 4) and (-1 < nc < 4):
                    memo = (nr, nc)
                    if bo[nr][nc] > 0:
                        update_queue(((nr,nc), pick, deepcopy(bo), depth+1))
                        card_update_flag = True
                        break
                        
            if (card_update_flag == False) and (memo != None):
                update_queue((memo, pick, deepcopy(bo), depth+1))