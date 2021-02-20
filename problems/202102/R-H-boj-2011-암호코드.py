N = input()
arr = []

for fig in N:
    arr.append(int(fig))

if N[0] == '0':
    print(0)
    exit()

dp = [1, 1]

for i in range(1, len(arr)):
    cnt = 0

    if arr[i] > 0:
        cnt += dp[-1]

    if 10 <= arr[i-1] * 10 + arr[i] < 27:
        cnt += dp[-2]

    dp.append(cnt % 1000000)

print(dp[-1])

'''
너무 지저분하게 예외처리를 하려고 했는데(문제를 풀어놓고 예외만 핸들하면 되겠지하는 생각..)

이게 점화식 하나 풀고 답이 다 나왔다고 생각하는...그런 오만한 태도에서 비롯된 것이 아닐까 싶다
걍 DP테이블에 0을 넣고 마지막까지 그 0이 계속 DP테이블에 남게 하면 되는 것이었다..
즉, 예외 자체도 DP테이블에서 자연스럽게 해소되도록 유도하는게 가장 좋은 방법임을 되세겨야 한다.

그리고 초기값을 약간 따로 채워줘야 하는 문제에서 예외적으로 DP를 채우는 코드 밖에서 해결하려고 하지 말고
DP테이블에 활용할 수 있는 가상값?이랄까를 넣어줘서 자연스럽게 DP순회만 해도 답이 나올 수 있게 유도하면 좋을 것 같다

너무 억지스럽게 풀려고 하면 나중에 디버깅이 너무 힘들다 => DP순회 밖 예외는 최소한으로 줄인다!
이 문제는 처음부터 다시 풀어보자 되게 괜찮은 문제인듯


n = input() 
arr = []

for i in n:
    arr.append(int(i))

dp = [1]

if arr[0] == 0:
    print(0)
    exit(0)
elif arr[1] == 0:
    if (arr[0] == 1 or 2):
        dp.append(1)
    else:
        print(0)
        exit(0)
else:
    dp.append(2)

for i in range(2, len(n)):
    if arr[i] == 0:
        if (arr[i-1] == 1) or (arr[i-1] == 2):
            tmp = dp[i-2]
        else:
            print(0)
            exit(0)
    else:
        tmp = dp[i-1]
        if 10 * arr[i-1] + arr[i] < 27:
            tmp += dp[i-2]
    dp.append(tmp)

print(dp[-1] % 1000000)
'''
