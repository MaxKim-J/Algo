import math

n = int(input())


def star(arr):
    result = []
    length = len(arr)
    last_line = (length * 2) * 2 - 1
    for i in range(length * 2):
        if i < length:
            side = (last_line - len(arr[i])) // 2
            result.append(' ' * side + arr[i] + ' ' * side)
        else:
            blank = last_line - len(arr[i-length]) * 2
            result.append(arr[i - length] + ' ' * blank + arr[i-length])
    return result


stars = ['  *  ', ' * * ', '*****']

N = int(math.log2(n//3))

for _ in range(N):
    stars = star(stars)

for i in stars:
    print(i)
