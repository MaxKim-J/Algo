n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for i in room:
  student = i - b
  count += 1
  if student > 0:
    count += (student // c)
    if  student % c > 0:
      count += 1
    

print(count)