n, m, k = map(int, input().split())
team = 0

while True:
  if n < 2 or m < 1:
    break
  n -= 2
  m -= 1
  team += 1

left = n + m
k -= left

if k > 0 :
  intern_in_left = k // 3 if k % 3 == 0 else (k // 3) + 1
  team -= intern_in_left

print(team)