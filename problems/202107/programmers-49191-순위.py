# i를 이긴 얘랑 진 얘의 합이 모든 남은 선수들 수면 i의 등수를 알 수 있다 => 는 성질을 이용
# i한테 이긴얘, 진얘를 저장해두는 집합 딕셔너리를 사용한다

def solution(n, results):
    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set() # 중복된 선수들이 계속 나올 수 있어 집합을 사용하면 좋음
        
    for i in range(1, n+1):
        # 경기를 순회하면서 진얘랑 이긴얘를 넣는다
        # 모든 선수들을 순회하면서 순회할때마다 result도 전부 순회하는 식이다
        for battle in results:
            if battle[0] == i:
                wins[i].add(battle[1])
                
            if battle[1] == i:
                loses[i].add(battle[0])
                
        # i에 해당하는 진, 이긴 상황을 다 넣은 다음에
        # i한테 진 선수들을 순회하며 wins 딕셔너리에 i가 이겼음을 다 표시한다
        for winner in loses[i]:
            wins[winner].update(wins[i])

        # i한테 이긴 선수들을 순회하며 lose 딕셔너리에 i가 졌음을 다 표시한다
        for loser in wins[i]:
            loses[loser].update(loses[i])
            
    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1
            
    return cnt