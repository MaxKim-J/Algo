# 큰그림 DP - 순서대로 생각해도 답이 나옴
# 전 집을 털고 가면 다음 집을 못털고, 전전집을 털었다면 현재 집을 털 수 있음 => 두개를 맥스
# 처음 시작할때 첫 집을 털면 맨 마지막 집을 못 터므로 두가지 경우로 크게 나눠서 구하기
# 테이블에는 각 집까지 털었다고 했을때의 최대값을 기록해야함

def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        
    dp1[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    return max(dp1[-2], dp2[-1])