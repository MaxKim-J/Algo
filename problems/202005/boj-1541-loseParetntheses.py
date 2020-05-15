# 백준 1541: 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 시간 : 15분
# 경과 : 맞았습니다(68ms)

sum_expressions = list(input().split('-'))
result = sum(map(int, sum_expressions[0].split('+')))

for i in range(1, len(sum_expressions)):
    sum_result = sum(map(int, sum_expressions[i].split('+')))
    result -= sum_result

print(result)

# * 그리디 : +로 이어진 곳들을 먼저 다 더해버린 후 수식에서 -만 남기면 가장 작은 값을 구할 수 있다
