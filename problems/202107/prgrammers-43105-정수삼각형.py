# 처음, 끝, 중간것들의 케이스를 나눠서 DP
# 파라미터 그대로 DP 테이블로 활용해주면 좋다
# max를 치기 전에, 그 다음 값의 경로가 겹치는지를 확인해보자(max 쳐도 상관이 없는 건지 뭔지)

def solution(T):
    for i in range(1,len(T)):
        for j in range(i+1):
            if j == 0:
                T[i][j] += T[i-1][j]
            elif j == i:
                T[i][j] += T[i-1][j-1]
            else:
                T[i][j] += max(T[i-1][j], T[i-1][j-1])
    return max(T[-1])