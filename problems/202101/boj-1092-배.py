n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

if max(crane) < max(box):
    print(-1)
    exit(0)

# 기록
positions = [0]*n
checked = [False] * m

crane.sort(reverse=True)
box.sort(reverse=True)

result = 0
count = 0
# 매분
while True:
    if count == len(box):
        break
    for i in range(n):
        while positions[i] < len(box):
            # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날때까지 반복
            # 하나 뽑히면 break
            if (not checked[positions[i]]) and (crane[i] >= box[positions[i]]):
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)
