N = input()
N = sorted(N, reverse=True)

sum = 0

if '0' not in N:
  print(-1)
else:
  for i in N:
    sum += int(i)
  if sum % 3 != 0:
    print(-1)
  else:
    print(''.join(N))

# 모든 자릿수의 합이 3의 배수 => 약간 공배수에도 적용이 되는 거같네... 30의 배수는 무조건 3의 배수이므로(충분조건)
# https://m.blog.naver.com/PostView.nhn?blogId=alwaysneoi&logNo=100200385519&proxyReferer=https:%2F%2Fwww.google.com%2F