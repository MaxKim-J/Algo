
#!!!!!! 부분수열의 정의 : 주어진 수열의 일부 항을 원래 순서대로 나열하여 얻을 수 있는 수열(연속합이랑 구분해야함)

#! 재귀를 사용하여 부분수열 합의 경우의 수를 탐색하는 방법인데,
#! 이 방법은 좌우측을 구한 후 while을 돌며 좌우합이 S만족하는지 체크하는 방식보다 효율적이다.
# * 투포인터 기법이 연속합이 아니라 부분수열 문제에 좋은지는 모르겠다. 자연수임이 보장되지 않은 경우는 더 그렇고


# ? 같이 연산할 수 있는 것은 한번에 하자는 철학
def dfs(start, end, value, direction):
    global result

    # 더이상 갈 곳이 없을 경우
    if start == end:
        # 왼쪽의 경우 왼쪽에서 모은 연속수열 합의 경우의 수를 업데이트
        if direction == 'left':
            try:
                dic[value] += 1
            except:
                dic[value] = 1
        # 오른쪽의 경우, 찾으려는 값 S에서 오른쪽에서 구한 부분합 값을 뺀 값을
        # 왼쪽에서 만들 수 있다면 그 경우의 수가 곧 S를 만드는 경우의 수가 된다. 그래서 그 경우의 수를 result에 더함
        # * 수열 탐색할때 dfs에 따르면 계속해서 아무것도 부분합으로 추가 안하고 0인 경우의 수도 존재 => 왼쪽이나 오른쪽에 부분합 답이 치우쳐있는 경우 커버
        # * 떨어져있는 부분수열의 원소들을 조합할때도 원 수열의 순서가 보장됨 => 딕셔너리의 값은 나눠진 두 수열의 부분수열의 합임을 보장하기 때문이다
        else:
            try:
                result += dic[S-value]
            except:
                pass
        return

    # 방문한 값을 포함할것인가 안할것인가로 DFS
    # 이경우 무조건 end는 포함하는 수열이 나온다
    #! 요기를 잘 기억할것. 부분수열 만들때 이런 재귀를 활용할 수 있다
    dfs(start+1, end, value, direction)
    dfs(start+1, end, value + arr[start], direction)


N, S = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
result = 0
# 배열을 두 부분으로 나눠 DFS 진행 => 2^20
#! 이것도 기술인듯..
leftStart, rightStart = 0, N//2

# 왼쪽의 가능한 합을 모두 구해서 딕셔너리에 저장한다
dfs(leftStart, rightStart, 0, 'left')

# 왼쪽의 가능한 합을 저장한 dict를 바탕으로, 오른쪽의 가능한 합을 구하고 경우의 수를 도출한다.
dfs(rightStart, N, 0, 'right')

# 찾고자 하는 값이 0일경우 결과중에 하나를 제한다
# 두개로 나눠진 수열 양쪽 모두에서 아무것도 골라지지 않았을때의 경우의 수가 하나 포함되었기 때문임
if not S:
    result -= 1

print(result)
