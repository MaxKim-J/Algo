n = int(input())

count = 1
stack, result = [], []

for i in range(1, n+1):
  data = int(input())
  while count <= data:
    stack.append(count)
    count += 1
    result.append('+')
  if stack[-1] == data:
    stack.pop()
    result.append('-')
  else:
    print('NO')
    exit(0)

print('\n'.join(result))
'''
스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인하기
정수 배열은 굳이 배열로 만들필요가 없다 숫자만 뽑아버리기
단순하게 만들려고 노력하기
'''