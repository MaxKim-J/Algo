# 가장 긴 증가하는 부분수열이랑 비슷하다
# 계산된 테이블 역추적 스킬

'''
벽돌을 무게기준으로 정렬

D[i] = 인덱스가 i인 벽돌을 가장 아래에 두었을때의 최대 높이
D[i] = max(D[i], D[j] + height) if area[i] > area[j]
기록을 하고 역추적을 해야함 높이를 빼면서

DP테이블의 인덱스는 block의 순서 => 이 index를 토대로 block을 특정할 수 있음
'''

n = int(input())
blocks = []
blocks.append((0, 0, 0, 0))

for i in range(1, n+1):
    area, height, weight = map(int, input().split())
    blocks.append((i, area, height, weight))

blocks.sort(key=lambda data: data[3])

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(0, i):
        if blocks[i][1] > blocks[j][1]:
            dp[i] = max(dp[i], dp[j] + blocks[i][2])

max_value = max(dp)
index = n
result = []

# 역추적
while index != 0:
    if max_value == dp[index]:
        result.insert(0, blocks[index][0])
        max_value -= blocks[index][2]
    index -= 1

print(len(result))
for block in result:
    print(block)
