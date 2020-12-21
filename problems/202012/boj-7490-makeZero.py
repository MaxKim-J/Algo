chances = int(input())


def solve(n, exp):
    global N
    if(n == N):
        end_exp = exp + str(N)
        if eval(end_exp.replace(' ', '')) == 0:
            print(end_exp)
        return
    solve(n+1, exp + str(n) + ' ')
    solve(n+1, exp + str(n) + '+')
    solve(n+1, exp + str(n) + '-')


for _ in range(chances):
    N = int(input())
    solve(1, '')
    print()

'''
동빈나 풀이
def recursive(array, n):
  if len(array) == n:
    operator_list.append(copy.deepcopy(array))
    return
  array.append(' ')
  recursive(array,n)
  array.pop()

  array.append('+')
  recursive(array, n)
  array.pop()

  array.append('-')
  recursive(array, n)
  array.pop()

test_case = int(input())

for _ in range(test_case):
  operators_list = []
  n = int(input())
  recursive([], n-1)

  integers = [i for i in range(1, n+1)]
  for operators in operators_list:
    string=""
    for i in range(n-1):
      strung += str(integers[i]) + operators[i]
    string += str(integers[-1])
    if eval(string.replace(" ","")) == 0
      print(string)
  print()
'''
