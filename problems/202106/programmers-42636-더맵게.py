import heapq

def solution(S, K):
    heap = []
    for s in S:
        heapq.heappush(heap, s)
        
    count = 0
    while True:
        h1 = heapq.heappop(heap)
        if h1 >= K:
            break
        if len(heap) < 1:
            return -1
        h2 = heapq.heappop(heap)
        new_h = h1 + (h2 * 2)
        heapq.heappush(heap, new_h)
        count += 1
    
    return count

# 자바스크립트에서 힙큐 어떻게 쓸것인지 생각해보기,,