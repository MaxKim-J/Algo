'''
백준 1759번, 암호 만들기

- 일단 완탐은 안됨 + 재귀는 맥시멈 콜때문에 안됨
- 그러면 BFS나 DFS, 혹은 DP일텐데, BFS의 경우는 visited를 쓰기가 애매
- 결국 DFS로 문자열 수에 맞는데 까지 내려가서 처리하는 방법으로 하면 재귀 스택 제한을 우회할 수 있음
'''


L, C = map(int, input().split())
figures = input().split()

alpha.sort()

path = []
all_path = []


def solve(depth, idx):
    if depth == L:
        all_path.append(''.join(map(str, path)))
        return
    for i in range(idx, C):
        # 탐색에 활용하는 DFS
        #! 이런 접근, 이런 DFS => 한번 밑에까지 내려갔을 때 그 단계를 다 처리함
        path.append(figures[i])
        solve(depth+1, i+1)
        # 처리가 되면 마지막 하나를 뺌
        path.pop()


def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return


solve(0, 0)
password(all_out)
