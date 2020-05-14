# 백준 11399: ATM
# https://www.acmicpc.net/problem/11399
# 시간 : 11분
# 경과 : 맞았습니다(68ms)

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 0

for i in range(N):
    result += sum(nums[:i+1])

print(result)

# * 모든 사람 atm 출금에 걸리는 시간을 최대한 줄이려면, 배열을 오름차순으로 정렬해서 수를 더해야함
# * 매번 가장 작은 수를 선택하게 되므로 그리디
