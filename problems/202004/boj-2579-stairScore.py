# 백준 2579: 계단 오르기
# https://www.acmicpc.net/problem/2579
# 시간 : 60분 초과
# 경과 : 런타임에러 => 틀렸습니다 => 못품

from sys import stdin

N = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(N)]

#! 예외처리 런타임에러 방지
if N < 3:
    result = sum(stairs)
else:
    dp = [stairs[0]]
    #! dp시작할때 초기값으로 얼마나 확보할지 정하기
    #! 이경우에는 전전전칸의 경우를 생각하므로 3개를 저장
    dp.append(dp[0] + stairs[1])
    dp.append(max(dp[0] + stairs[2], stairs[1]+stairs[2]))

    for i in range(3, N):
        # 전칸에서 올라왔거나 전전칸에서 올라온 경우의 max값
        # 전전칸 : 지금계단 + 전전계단까지의 최대값
        # 전칸 : 지금계단 + 전계단 + 전전전계단까지의 최대값
        dp.append(max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2]))
    result = dp[-1]
print(result)

#! 어딜 기준으로 생각해야하는지 확실하게 정하자(앞? 뒤?) => 거기까지 왔을 때 어떻게 온걸까에 대한 작은 문제
#! 명징하고 논리적으로 개연성있게 생각하기 => 이건가???하고 찍는거 의미없음 시간만 나감

#! 이렇게 풀려고 했었는데 틀렸습니다 나옴
# * 어떤 칸 있을때 전칸에서 온 경우 전전칸에서 온경우 나눠서
# * 만약에 저번에 전칸에서 왔을 경우 그 다음은 전전칸에서 오게 하는 그런 거였는데...
# ? 왜틀렸는지 모르겠음 물론 위의 풀이가 더 명징하긴 함
"""
if N < 3:
    result = sum(stairs)

else:
    stairs[1] += stairs[0]
    flag = True
    for idx in range(2, N):
        # print(flag)
        if flag:
            stairs[idx] += stairs[idx-2]
            flag = False
        else:
            if stairs[idx-2] >= stairs[idx-1]:
                stairs[idx] += stairs[idx-2]
            else:
                stairs[idx] += stairs[idx-1]
                flag = True
        # print(stairs)
        # print()
    result = stairs[-1]

print(result)
"""
