N = int(input())
distances = []

for _ in range(N):
    distances.append(list(map(int, input().split(' '))))

# 최대 계산 개수는 10^10이므로 모두 순회는 할 수 없고, 백트랙킹으로 안될거같은 순회를 다 떨궈내야함

# 최대 경로의 거리는  1000000(최대 거리의 수) * 10(다시 자기까지 오는 최대 경로의 수) = 천만 + 1
min_value = 10000001

#! 조건 잘보자... 처음 시작했던 곳으로 딱! 와야 끝남


def recursion(start, visited, distance):
    global min_value, distances, N
    last_visit = visited[-1]
    if len(visited) == N:
        if distances[last_visit][start] != 0:
            min_value = min(min_value, distance +
                            distances[last_visit][start])
            return
    for (i, value) in enumerate(distances[last_visit]):
        if (value != 0) and (i not in visited):
            recursion(start, visited + [i], distance + value)


for i in range(N):
    recursion(i, [i], 0)

print(min_value)
