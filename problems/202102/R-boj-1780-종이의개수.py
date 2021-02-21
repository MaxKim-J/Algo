# 구현력이 딸림 + 좀더 문제에 붙어서 구현해야했음

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
result = {0: 0, 1: 0, -1: 0}


def solve(x, y, n):
    num_check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            # 한 종이는 같은 수로 이루어져있을 때 한 조각으로 사용할 수 있으므로
            # 일단 한 재귀 스택에서 먼저 모든 이차원 배열의 수를 순회하여 다 같은 수인지 확인하기
            # 순회를 하다가 어떤 한 값이라도 다르다면 => 그 테이블 탐색 멈추고 9개 테이블로 분해함
            if(paper[i][j] != num_check):
                # 그 값을 기준으로 9개의 서브 테이블로 분해
                for k in range(3):
                    for l in range(3):
                        # x랑 y에다가 더하는것
                        solve(x + (k * n//3), y + (l * n//3), n//3)
                # 그리고 결과산출 안함
                return

    result[num_check] += 1


solve(0, 0, N)

print(result[-1])
print(result[0])
print(result[1])
