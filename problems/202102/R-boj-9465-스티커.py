# 왼쪽에서 오른쪽으로
# 순서가 별로 상관없는 입력이라도, 순서와 상관있게 만들고 생각하기
# 받은 입력 그대로 DP
#! 테이블의 x => 얘가 마지막으로 선택된 요소일때 앞에서 뭐를 뽑았을지를 생각하기(이런 유형 많은듯..)

'''
귀납적으로 DP 점화식 구하기

https://sungmin-joo.tistory.com/42

1. DP로 풀수 있는 문제는 일관된 순서를 테이블에 표현할 수 있는 경우임(왼쪽에서 오른쪽이라던지..)
2. 경우의 수가 어떻게 진행되는지 일단 생각해봐야함 그게 먼저임 => 어디서 시작해서 어디로 갈 수 있는 경우의 수 그게 dp(n)
3. 그리고 그거 몇개 구해놓은 다음에 dp(n-1)이랑 dp(n-2)를 살펴보면서 경계점을 구해보기
'''

t = int(input())
for i in range(t):
    dp = []
    n = int(input())
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))
