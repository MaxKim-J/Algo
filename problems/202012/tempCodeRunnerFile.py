chances = int(input())


def solve(n, exp):
    global N
    if(n == N):
        end_exp = exp + str(N)
        if eval(end_exp.replace(' ', '')) == 0:
            print(end_exp)
            return
        else:
            return
    solve(n+1, exp + str(n) + '+')
    solve(n+1, exp + str(n) + '-')
    solve(n+1, exp + str(n) + ' ')


for _ in range(chances):
    N = int(input())
    solve(1, '')
    print()