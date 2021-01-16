from collections import deque

A, B, C = map(int, input().split())
visited = [[0] * 201 for i in range(201)]
# 계수정렬을 써도 좋을 것 같다
result = []
queue = deque([(0, 0, C)])

# 삼항연산자 사용하는거 기억하자


def enable_node(a, b, c):
    result = []
    # b -> a
    result.append((A, b-(A-a), c) if a+b > A else (a+b, 0, c))
    # a -> b
    result.append((a-(B-b), B, c) if a+b > B else (0, a+b, c))
    # a -> c
    result.append((a-(C-c), b, C) if a+c > C else (0, b, a+c))
    # c -> a
    result.append((A, b, c-(A-a)) if a+c > A else (a+c, b, 0))
    # b -> c
    result.append((a, b-(C-c), C) if c+b > C else (a, 0, c+b))
    # c -> b
    result.append((a, B, c-(B-b)) if c+b > B else (a, c+b, 0))
    return result


while queue:
    a, b, c = queue.popleft()
    for x, y, z in enable_node(a, b, c):
        # x,y의 물 양이 결정되면 z도 바로 알 수 있는, z가 (x,y)에 종속성을 갖는다는게 중요했다
        if visited[x][y] == 0:
            if x == 0:
                result.append(z)
            # 굳이 z까지 queue에 넣을 필요는 없는 것 같다. xy로 z가 유추 가능하기 때문에
            # 근데 시간 넉넉할거 같아 걍 편하게 했음
            queue.append((x, y, z))
            visited[x][y] = 1

result.sort()
print(' '.join(map(str, result)))
