# 백준 1300 K번째 수
# https://www.acmicpc.net/problem/1436
# 시간 : 40분
# 경과 : 맞았습니다(1076ms)


N, K = int(input()), int(input())
start, end = 1, N**2

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in range(1, N+1):
        # 열의 숫자 초과 불가능
        temp += min(mid//i, N)

    if temp >= K:
        answer = mid
        # 다음 미드값 감소
        end = mid - 1
    else:
        # 다음 미드값 증가
        start = mid + 1
print(answer)

# * 때려맞춤;;
#! 접근1) A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.(너무나 당연)
#! 접근2) 이분탐색은 지가 알아서 끝난다 (while문) : 이분탐색이 진행되는 마지막 값이 곧 답
#! 뭔가 좋은 접근이라서 가져와봄
"""
예를 들어 10 * 10에서 20보다 작거나 같은 수를 생각해보자.
1*1~1*10
2*1~2*10
3*1~3*6
...
10*1~10*2

위 수가 존재할텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.
20//1: 10개 --> 단 열의 숫자(N*N배열이므로)를 초과할 수 없다.
20//2: 10개
20//3: 6개
...
20//10: 2개

따라서 이를 식으로 표기해보면 아래와 같다.
temp = 0
for i in range(1, N+1):
        temp += min(mid//i, N)
"""
