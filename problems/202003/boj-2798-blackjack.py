# 백준 2789번 블랙잭
# https://www.acmicpc.net/problem/2798
# 시간 : 40분
# 경과 : 맞았습니다

import sys

data_num, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

min_abs = M
result = 0

for first_card in cards:
    second_cards = cards[:]
    second_cards.remove(first_card)
    for second_card in second_cards:
        third_cards = second_cards[:]
        third_cards.remove(second_card)
        for third_card in third_cards:
            total = first_card + second_card + third_card
            new_abs = abs(total-M)
            if new_abs <= min_abs and total <= M:
                min_abs = new_abs
                result = total
print(result)

#! 접근1 - 내가 푼데로 리스트를 이용하면 코딩은 쉽지만, 이미 반복된 조합을 조금은 더 반복해야함
# * 리스트 말고 레인지로 하는게 낫긴 할듯, 어쨋든 브루트 포스를 이용하려면 for문을 세개를 겹쳐야 한다
'''
N, M = map(int, input().split())
card = list(map(int,input().split(' ')))
answer = 0
for i in range(0, N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (card[i]+card[j]+card[k]) <= M and M - (card[i]+card[j]+card[k]) < M - answer:
                answer = card[i]+card[j]+card[k]
print(answer)
'''
# * 반복을 피할 수 없다면 어떻게 짜야 반복을 최대한 줄일 수 있는지 생각해야한다
# * 여기서 레인지는 첫번째로 선택한 것의 뒤만 보면 된다는 전제를 이해하고 쓰인 것.
