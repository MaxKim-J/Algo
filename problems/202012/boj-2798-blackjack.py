import sys

length, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))

result = 0
length = len(arr)

for i in range(length):
    for j in range(i+1, length):
        for m in range(j+1, length):
            sum_value = arr[i] + arr[j] + arr[m]
            if sum_value <= M:
                result = max(result, sum_value)
print(result)

'''
n은 최대 100개 => 1초에 이천만개의 연산 수행 가능함
삼중반복문이라고 해도 100*100*100 = 1000000개 => 삼중 반복문 때리기
=> 이런 판단이 지금 중요
max함수 사용하기

'''
