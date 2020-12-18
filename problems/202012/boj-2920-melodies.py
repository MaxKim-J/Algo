import sys

melodies = list(map(int, sys.stdin.readline().split(' ')))
result = ''

for i in range(len(melodies) - 1):
    substract = melodies[i+1] - melodies[i]
    if substract == 1:
        result = 'ascending'
    elif substract == -1:
        result = 'descending'
    else:
        result = 'mixed'
        break

print(result)

'''
변수를 최대한 적게 쓰는게 좋은거 같다 그리고 문제의 조건 잘 반영하기

for i in range(1,8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
'''
