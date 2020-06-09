# 백준 7490번 0 만들기
# https://www.acmicpc.net/problem/4195
# 시간 : 30분
# 경과 : 틀렸습니다 -> 맞았습니다(136ms)
# * 나동빈 문제


def find_zero(new_num, expression):
    global limit, result
    if new_num > limit:
        if eval(expression.replace(" ", "")) == 0:
            result.append(expression)
        return

    find_zero(new_num+1, expression + "+" + str(new_num))
    find_zero(new_num+1, expression + "-" + str(new_num))
    find_zero(new_num+1, expression + " " + str(new_num))


test_case = int(input())
for _ in range(test_case):
    limit = int(input())
    result = []
    find_zero(2, "1")

    result.sort()
    for i in result:
        print(i)
    print()

#! 재귀로 가능한 모든 경우의 수 완전탐색하는 문제
#! replace와 eval 머리에 박고 가자
#! 처음에 틀렸습니다 나온 이유 : 값을 같이 계산하면서 가려고 했는데 그러면 합쳐지는 숫자 계산 못함
