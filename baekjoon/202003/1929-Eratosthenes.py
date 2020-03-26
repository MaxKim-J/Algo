# 백준 1929번 소수 구하기 - 에라토스테네스의 체 사용
# 개념 읽고 코드로 구현해 본다
# 실패해따.. 그냥 좋은 방법을 공부하자;;
# 배열의 인덱스를 이용하는 방법

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    # 거까지만 해도 충분함 
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            # 와 i+i부터 시작해서 i씩 뛰는거 생각 넘 좋다;
            for j in range(i+i, n, i): 
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

min_n, max_n = map(int, input().split())
#! 접근1): 이런 문제에서는 배열이 한정되어 있는게 낫다는 생각을 했어야함.
#! 접근2): range로 배수 삭제 구현하는거 너무 좋은 방법인듯
#! 접근3): 배열의 인덱스를 이용한 값 저장 방법을 기억하자 

#* 한번에 다 처리하는게 가끔 더 나을때도 있다. 몇줄 필요 없는거였는데;