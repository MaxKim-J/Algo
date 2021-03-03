'''
0이랑 1 : 1을 곱하면 최대를 만들 수 없으므로 그냥 더하기
양수 : 짝지어서 곱하고 홀수면 더하기
음수 : 짝지어서 곱하고 홀수면 더하기

짝지어 더하는 함수 만들어서 배열에서 음수랑 1이상 양수 분리해서 결과 구하고
원래 배열에 0이랑 1이 있으면 더해준다

이때 0이 있는데 음수 리스트 길이가 홀수면 마지막 음수를 0으로 없애줄 수 있다
'''

def match_and_sum(arr, types):
  global g_arr
  result = 0
  for i in range(0, len(arr), 2):
    if i + 1 == len(arr):
      if (types == 'minus') and (0 in g_arr):
        break
      result += arr[i]
      break
    result += (arr[i] * arr[i+1])
  return result

n = int(input())
g_arr = []

for _ in range(n):
  g_arr.append(int(input()))

minus_arr = sorted(list(filter(lambda x: x < 0, g_arr)))
plus_arr = sorted(list(filter(lambda x: x > 1, g_arr)), reverse=True)
result = match_and_sum(minus_arr, 'minus') + match_and_sum(plus_arr, 'plus')

result += g_arr.count(1) # 와...중복 가능함 오졌다 문제 너무 더럽다ㅜㅜㅜ

print(result)


