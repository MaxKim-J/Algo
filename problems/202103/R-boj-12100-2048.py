import sys, copy

input = sys.stdin.readline
'''
한 열씩 보는게 맞는 접근이었음
요번에도 방향은 숫자로 표현하기
'''

# 열 한줄씩 보기
#! 방향으로 합치는 로직은 거의 같은데 시작점이 다름
def move(dir):
    # 상
    if dir == 0:
        for j in range(n):
            # 앞줄(가장 먼저 합쳐질 타겟줄)
            idx = 0
            for i in range(1, n):
                # 다음줄 => 0이면 무시함 걔는 거기서 뭐 할 필요가 없음
                if a[i][j]: 
                    # 다음줄 수 저장 한 후
                    temp = a[i][j]
                    # 다음줄을 0으로 만들고 앞줄을 타진해봄
                    a[i][j] = 0
                    # 앞줄이 0이면 => 바로 뒷줄값 대입하고 idx를 움직이지 않음(0을 건너뛰기 위한 전략), 다음줄을 가리키는 i 포인터는 다음 순회에서 움직임
                    # 만약 i가 같은 수일 경우 0 뛰어넘고 바로 합칠 수 있게끔
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    # 앞줄의 수가 뒷줄과 같다면 => 더해서 넣은 후 다음 줄로 이동
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        # 다음줄은 아래로 내려감
                        idx += 1
                    # 앞줄 수가 뒷줄과 다르다면 => idx를 다음줄로 이동하고 다음줄로 이동한 idx에 i를 위로 올림(합칠수 없고 뛰어넘은 위치 사이에는 언제나 0이 있으므로)
                    else:
                        idx += 1
                        a[idx][j] = temp

    # 하
    elif dir == 1:
        for j in range(n):
            idx = n-1
            # n기준으로 -2를 해야 맨 마지막줄에서 다음줄 나올 수 있음 => 거기서부터 시작해서 위로 올라옴
            for i in range(n - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        # 다음줄은 위로 올라옴
                        idx -= 1
                    else:
                        idx -= 1
                        a[idx][j] = temp

    # 좌
    elif dir == 2:
        for i in range(n):
            idx = 0
            # 열 기준으로 0에 가까운 방향으로 이동할것(1부터 시작)
            for j in range(1, n):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        # 다음줄은 오른쪽
                        idx += 1
                    else:
                        idx += 1
                        a[i][idx] = temp

    # 우
    else:
        for i in range(n):
            idx = n-1
            for j in range(n - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        a[i][idx] = temp

# DFS, 한번 순회할때 4방향 다함 depth 5까지
def dfs(cnt):
    global a, ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, a[i][j])
        return

    temp_a = copy.deepcopy(a)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        a = copy.deepcopy(temp_a)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0)
print(ans)