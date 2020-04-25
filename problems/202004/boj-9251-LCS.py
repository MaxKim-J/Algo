# 백준 9251 : LCS
# https://www.acmicpc.net/problem/9251
# 시간 : 60분+
# 경과 : 못품

import sys

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)

matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])

#! 이차원 배열을 모두 채우고 그 끝값을 리턴하는 로직인데, 이차원 배열이 규칙이 있음
#! 같은 수가 추가되었을 경우 대각선값을 그대로 가져와 +1하고
#! 다른 수가 추가되었을 경우 지금까지 추가되었던 전 값(위, 옆값)중에 큰 걸 가져온다

# * 참고 : https://suri78.tistory.com/11
