# 백준 1011 fly me to the alpha Centauri

# 순서를 못찾겠으면 일단 쭉 노가다를 뛰어라,,,
# 범위값에 해당하는 것으로 승부보기, 횟수랑 연관성 파악하기
# 답에 가장 가까운 변수가 뭔지 파악하기

def warp(dist):
    minN = powN = maxN = warpCnt = 0; n = 1
    while True:
        powN = n**2;
        minN = powN - n + 1
        maxN = powN + n
        if minN<=dist<=maxN:
            if minN<=dist and dist<=powN:
                warpCnt = (n**2) - 1
            else:
                warpCnt = n**2
            break
        n+=1
    return warpCnt 

data_num = int(input())
result = []

for _ in range(data_num):
    line = input().split();
    x, y = int(line[0]), int(line[1])
    dist = y-x
    result.append(warp(dist))

for i in result:
    print(f"{i}")
