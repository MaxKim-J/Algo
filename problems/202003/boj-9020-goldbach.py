#  백준 9029-골드바흐의 추측
# https://www.acmicpc.net/problem/9020
# 시간 : 1시간 => 못품
# 경과 : 시간초과 => 시간초과 => 맞았습니다
# 제한시간 : 4660ms

import sys

input_count = int(sys.stdin.readline())

for _ in range(input_count):
    target_num = int(sys.stdin.readline())
    substract = target_num

    seive = [False, False]+ [True]*(target_num - 1)
    for idx in range(2, int(target_num**0.5)+1):
        if seive[idx]:
            for i in range(idx+idx, target_num+1, idx):
                seive[i] = False

    for i in range(target_num//2, 1, -1):
        if (seive[i] == True) and (seive[target_num-i] == True):
            print(i, target_num-i)
            break

#! 접근1) 빠르게 소수를 구해야 하는 알고리즘은 무족권 에라토스테네스가 답임
#* 생각해보면 이 방법 생각 할 수 없었다기 보단 하기 귀찮아서 계속 안하다가 시간만 보낸듯?

#! 접근2) range뒤에서부터 접근하는 것도 순회의 좋은 방법이다 
#* 마지막 답 낼때 뒤에서 -1씩 접근하면 무조건 i가 target_num-i보다 클수밖에 없고
#* 가장 먼저 발견한 소수쌍이 가장 차의 절대값이 작을 수밖에 없음(i가 작아질수록 커지기때무네..)
#* "그럴수밖에 없는 상황"을 잘 활용해야 할듯
    

