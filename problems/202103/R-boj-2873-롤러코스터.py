'''
일단 최대한 많은 지점을 방문해서 목적지까지 가야 하고
결국에 다 방문할 수 있다면 다 방문하는 것이 최고의 방법

일단 BFS가 먼저 생각났는데, 
최대입력이 백만칸이고 모든 칸을 다 순회해봐야 하므로 4^100만이 최소 하나 나올때까지 답은 안나올 것인데
1초가 시간제한이므로 절대 안됨 시간초과남

홀수의 행과 열의 개수라면 모두 방문할 수 있음
또는 행과 열의 개수가 하나라도 홀수라면 모두 방문 가능
행과 열이 모두 짝수라면 모든 점을 방문할 수 없음. 하지만 한 점을 제외한다면, 한 점을 제외한 모든 점을 방문할 수 있음
=> 이때 가장 작은 한 점을 제외하고 모든 점을 방문하면 됨

가장 작은 한 점이 충족해야할 조건 == i + j가 홀수인 지점만 가능함
이런 지점들의 최소 지점을 구한 후 해당 지점을 방문하지 않도록 해주면 됨

지점을 골랐다면, 해당 점이 있는 지점 묶음을 기준으로 몇가지 방식으로 나누어 순회를 하면 됨(방법은 여러개가 가능)
'''

import sys
 
r, c = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

## 둘중에 하나라도 홀수일 경우 => 걍 한번에 방문하는 시나리오를 바로 출력해주면 됨
if r % 2 == 1:
    sys.stdout.write( ('R'*(c-1) + 'D' + 'L'*(c-1) + 'D')*(r//2) + 'R'*(c-1) )
elif c % 2 == 1:
    sys.stdout.write( ('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(c//2) + 'D'*(r-1) )
## 둘다 짝수인 경우
elif r % 2 == 0 and c % 2 == 0:
    # find position to jump
    # 홀수격차칸 중 최소를 구함 => 이 아이디어가 무척 핵심적이었던 것 같음
    low = 1000
    position = [-1, -1]
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]
        elif i % 2 == 1:
            for j in range(0, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]
    
    # 지점에과 같은 column에 닿기 전에 반복되는 경로를 일단 뿌려줌
    res = ('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(position[1]//2)

    # 지점을 피해서 가는 경로 => 어캐짯어.........ㅜㅜㅜㅜㅜㅜㅜㅜ
    # 일단 가장 맨 위로 보내서 U를 할일을 없앴음'
    # 얘는 직접 그 지점을 피하는 과정을 구현해야함
    x = 2 * (position[1]//2)
    y = 0
    xbound = 2 * (position[1]//2) + 1
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound-1] != position:
            x -= 1
            res += 'L'
        if y != r-1:
            y += 1
            res += 'D'
 
    # 지점을 찍은 후의 경로
    res += ('R' + 'U'*(r-1) + 'R' + 'D'*(r-1))*((c-position[1]-1)//2)
 
    print(res)

#! 코테 기준으로 공부를 하고 있지만....... 
#! 내생각엔 플래티넘 3까지만 풀 수 있으면 코포 블루 이상이랑 코테 60%이상 합격정도는 쌉가능일거같다
#! 플래티넘 3을 목표로 공부하자