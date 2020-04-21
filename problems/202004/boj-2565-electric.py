# 백준 2565: 전깃줄
# https://www.acmicpc.net/problem/2565
# 시간 : 35분
# 경과 : 틀렸습니다 => 맞았습니다(76ms)

# * 정렬한다음에 최장증가수열 찾으면 댐
# * 이제 증가수열은 좀 감 잡은듯...

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
arr_modified = list(map(lambda x: x[1], arr))

dp = [0]*N

for i in range(N):
    for j in range(i):
        if (arr_modified[j] < arr_modified[i]) and (dp[i] < dp[j]):
            dp[i] = dp[j]
    dp[i] += 1

print(N - max(dp))


"""
#* 처음풀이
#! 솔직히 이걸로 왜안풀리는지 진짜 모르겠음
#! 위에 풀이랑 정반대로 한 생각인데 오름차순해서 최장 감소수열 찾는거...
#! 그냥 감소수열로 풀 수 있는건 증가수열로도 풀 수 있으니까 접근성 좋은 방법 택하자

arr.sort(reverse=True)
arr_modified = list(map(lambda x: x[1], arr))

for i in range(1, N):
    if min(arr_modified[:i]) < arr_modified[i]:
        arr_modified[i] = 501

print(arr_modified.count(501))
"""
