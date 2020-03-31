#  백준 4948 베르트랑 공준
# #ttps://www.acmicpc.net/problem/4948
# 시간 : 43분
# 경과 : 시간초과 => 맞았습니다 
# 제한시간 : 시간초과 => 2432 ms => 2360 ms

import sys

# main
while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break

    # 이것의 최적화,,,
    if num == 1:
        print(1)
        continue

    result = [False, False] + [True] * (2*num - 1)

    for i in range(2, int((2*num)**0.5)+1):
        if result[i]:
            for n in range(i+i, 2*num, i):
                result[n] = False
    print(len(list(filter(lambda x:x==True, result[num+1:2*num]))))

#* 아이디어 : 사실 구간별로 잘라서는 소수를 구할 수 없으니 1부터 배열을 설정하고
#* 최대 범위까지 소수를 구해놓은 다음에 리스트 일부의 길이를 제공하는 방식

#! 개선1) : 딱히 최소 소수를 찾는 함수는 없어도 된다 배열 인덱스를 이용하면
#! 개선2) : for 문 없이 배열 슬라이스 치환으로도 할 수 있는 것 같은데 코드스니펫에 정리

#? 1입력했을 때 최적화가 안되서 예외로 따로 뺐는데 얘를 통합시킬 수는 없을까 
