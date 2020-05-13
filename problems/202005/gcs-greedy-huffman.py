# 갓찬수 Greedy: 허프만 트리
# 시간 : 30분


from heapq import heappush, heappop

min_heap, result_heap = [], []
char_dict = {'a': 43, 'b': 13, 'd': 16, 'c': 12, 'e': 9, 'f': 5}

for key in char_dict.keys():
    heappush(min_heap, (char_dict[key], key))
    heappush(result_heap, (char_dict[key], key))

print(min_heap)

while len(min_heap) > 1:
    least = heappop(min_heap)
    second_least = heappop(min_heap)
    new_tuple = (least[0] + second_least[0], None)
    heappush(min_heap, new_tuple)
    heappush(result_heap, new_tuple)

print(result_heap)
