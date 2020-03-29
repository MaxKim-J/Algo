# 백준 2447번 별찍기-10
# https://www.acmicpc.net/problem/2447
# 시간 : 1시간 - 못품
# 경과 : 못품


def stars(n):
    matrix = []
    # 몇줄 만들거?
    for i in range(3 * len(n)):
        # 문제의 규칙 : 이게 1이면 중간지대임(비워놓아야 하는 칸)
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        # 문제의 규칙 : 이게 1이 아니면 위랑 아래(채워야 하는 칸)
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))


star = ["***", "* *", "***"]

n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)

for i in star:
    print(i)

#! 접근1 ) 재귀만으로 풀려고 해서는 안된다 => 규칙을 찾다보니 재귀를 적용시킬 것이다 라는 마인드
# * len을 어떤 식으로 이용할 수 있을지 + 규칙 생각하기

#! 접근2) 재귀 문제란게 리턴값에만 재귀를 적용시키는 것은 아니다
'''
for i in range(k):
    star = stars(star)
'''
# * 요런 것도 어찌보면 재귀의 일종이 될 수 있음(재귀로 나온 값을 그대로 다시 넣기)
