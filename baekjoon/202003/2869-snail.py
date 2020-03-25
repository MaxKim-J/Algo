# 백준 2869 : 달팽이는 올라가고 싶다 풀이 
# https://www.acmicpc.net/problem/2869
# 시간 : 40분
# 경과 :  시간초과 - 시간초과 - 맞았습니다

# 이런걸 좀 더 깔끔하게 풀 순 없을까 고민해야할듯
# 반복문이 꼭 필요한건 아니더라 
# a,b,v를 넣으면 답이 바로 나오는 구조라는 것을 바로 알아야함 제한시간 보고

import math

A,B,V = map(int, input().split())
days = math.ceil((V-A)/(A-B)) + 1
print(days)