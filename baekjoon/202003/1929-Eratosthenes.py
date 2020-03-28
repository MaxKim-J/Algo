# 백준 1929번 소수 구하기 - 에라토스테네스의 체 사용
# 개념 읽고 코드로 구현해 본다
# 실패해따.. 그냥 좋은 방법을 공부하자;;
# 배열의 인덱스를 이용하는 방법

min_n, max_n = map(int, input().split())

result = [False, False] + [True] * (max_n - 1)

for i in range(2, int(max_n**0.5)+1):
    if result[i]:
        for n in range(i+i, max_n+1, i):
            result[n] = False
prime_list = [ind for ind in range(min_n, max_n+1) if result[ind]]

for i in prime_list:
    print(i)


#! 접근1): 이런 문제에서는 배열이 한정되어 있는게 낫다는 생각을 했어야함.
#! 접근2): range로 배수 삭제 구현하는거 너무 좋은 방법인듯
#! 접근3): 배열의 인덱스를 이용한 값 저장 방법을 기억하자 

#* 한번에 다 처리하는게 가끔 더 나을때도 있다. 몇줄 필요 없는거였는데;