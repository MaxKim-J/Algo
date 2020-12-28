height, width = map(int, input().split())
height_result, width_result = [0]*height, [0]*width

for i in range(height):
    guards = input()
    for j in range(width):
        if guards[j] == 'X':
            width_result[j] += 1
            height_result[i] += 1

print(max(width_result.count(0), height_result.count(0)))
