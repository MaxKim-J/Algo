'''
closest point

y축과 나란하게 직선을 그어 평면을 둘러 나누고, X좌표 기준으로 정렬한 다음 n/2번째와 n/2+1번째 점의 x좌표 평균을 기준 직선으로 잡음
그러면 두 점 모두 왼쪽에 속하는 경우, 두 점 모두 오른쪽에 속하는 경우, 양쪽에서 한점씩 나오는 경우 이렇게 3가지 경우의 수가 나옴
이 모든 경우에 대하여 최솟값을 구한 다음 세가지 중 제일 작은게 문제의 최종 정답이 됨
그런데도 각 최소값을 비교하는데 O(n^2)씩 드므로, 절대 답이 되지 않을 것 같은 쌍을 제거하고 남은 쌍에 대해서만 계산할 필요가 있음

그래서 두 점이 다 한쪽에 속하는 경우 거리의 최솟값의 min인 d보다 거리가 큰 3번 경우의 쌍은 비교하지 않으면 됨
따라서 기준선을 중심으로 좌우 거리 d이내에 들어오는 점기리만 비교하면 됨
그리고 그걸 y좌표 기준으로 정렬한 뒤 각 점을 자기보다 y좌표가 같거나 높은 것들을 비교하다가
y좌표의 차가 d이상이 되면 그 점에 대한 비교를끝내면 됨 (O(nlogn))
'''

# ** 공간을 나누는 분할정복 방법 배우기 **

import sys

# 거리 구하는 함수


def dist(x1, x2):
    return (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2


def solve(coords, N):
    # * 점 개수가 그냥 두개면 그 두 거리만 비교하면 됨
    if(N == 2):
        return dist(coords[0], coords[1])
    # * 3개면 그 3개중에 최소 출력
    elif(N == 3):
        return min(dist(coords[0], coords[1]), dist(coords[1], coords[2]), dist(coords[0], coords[2]))

    # * 4개 이상일 경우 들어가는 방법
    #! 일단 X좌표의 중간을 기준으로 기준선 좌표를 구한다
    mid = (coords[N//2][0] + coords[N//2-1][0]) // 2
    #! 중간을 기준으로 계속 나누면 점이 2,3개씩 나눠질때까지 재귀로 거리의 최솟값을 구할 수 있음 => 공간을 나누는 재귀
    d = min(solve(coords[:N//2], N//2), solve(coords[N//2:], N//2))

    #! 기준선 양쪽에 점이 걸쳐져 있는 경우를 구한다
    #! x의 범위 d 안쪽으로 제한
    # 일단 x를 평가했을때 가능한 점들을 다 배열에 넣어놓고 시작
    short_check = []
    for subset in coords:
        # 현재 좌표들중 중간 좌표와의 x거리가 d 이하일 경우
        # ? 제곱하는 이유는 dist 보면 루트가 없음 => 짜피 리턴해야하는 값이 제곱이므로
        if((mid - subset[0])**2 <= d):
            short_check.append(subset)
    # x좌표 기준 정렬
    short_check.sort(key=lambda x: x[1])

    #! y의 범위도 제한 - 두 점의 y좌표 차가 d이상이 되면 d보다 큰 경우이므로 제외한다
    # 평가해야할 좌표가 1개인 경우에는 뭘 할 수가 없다
    if(len(short_check) == 1):
        return d
    else:
        # 일단 d보다는 무조건 작아야만 답을 비빌수가 있음
        y_check = d
        # 아까 구해놓았던 가능한 좌표들에 대해 n^2 모두 순회하며 거리의 최솟값을 구한다
        for i in range(len(short_check) - 1):
            for j in range(i+1, len(short_check)):
                #! 두 점의 y좌표 차가 d이상이 되면 d보다 큰 경우이므로 아예 글러먹은 경우 제외
                if(short_check[i][1] - short_check[j][1]) ** 2 > d:
                    break
                #! 두 점을 골랐을 때 같은 쪽에 있는 경우 제외(d기준으로 거를때 섞여들어갈 수 있다)
                elif(short_check[i][0] < mid and short_check[j][0] < mid):
                    continue
                elif(short_check[i][0] > mid and short_check[j][0] > mid):
                    continue
                # 두 점의 거리를 구해 최소값 비교
                y_check = min(y_check, dist(short_check[i], short_check[j]))

    return y_check


N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

# ???? 중복을 제외한 배열과 그냥 입력 배열의 길이가 다르면? 걍 0출력하고 끝냄 - 여기 왜이러는거지
coords_set = list(set(map(tuple, coords)))
if len(coords_set) != len(coords):
    print("0")
else:
    # 중복을 제거한 집합 배열을 정렬한 후 돌린다
    coords_set.sort()
    print(solve(coords_set, N))
