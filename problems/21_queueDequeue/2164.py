# 직접만든 큐

import collections


class CardsQueue:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            return -1

    def enqueue(self, val):
        self.items.append(val)

    def bottom(self):
        return self.items[0]


cards = int(input())
cq = CardsQueue([i+1 for i in range(cards)])

while len(cq) > 1:
    cq.dequeue()
    cq.enqueue(cq.dequeue())

print(cq.bottom())

# collections로 데크 이용하면 시간 단축됨

card_num = int(input())
card_deque = collections.deque([i for i in range(1, card_num + 1)])

while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])
