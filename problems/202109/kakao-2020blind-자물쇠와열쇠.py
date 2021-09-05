# 핵심 아이디어는 잘 도출함 => 돌리고 옮기나 옮기고 돌리나 똑같다
# 2시간 걸림ㅜ

# n과 m을 구분했어야 했는데
# 유일한 테스트 케이스가 n과 m이 같은 경우라서 고려를 못했다. 
# 핵심 아이디어에서 어떤 변수가 어던 역할을 하는지 제대로 설정하고 가야한다
# 테스트케이스에 휘둘리지 말것
def enhance(arr, n, m):
    row = [[0] * (m+(n-1)*2) for _ in range(n-1)]
    arr = list(map(lambda r:[0] * (n-1) + r + [0] * (n-1), arr))
    return row + arr + row

def turn(arr):
    m = len(arr)
    result = [[] for _ in range(m)]
    for i in range(m-1,-1,-1):
        for j in range(m):
            result[j].append(arr[i][j])
    return result
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    e_key = enhance(key, n, m)

    hole = []
    for r in range(n):
        for c in range(n):
            if lock[r][c] == 0:
                hole.append((r,c))
                
    em = len(e_key)
    for _ in range(4):
        for i in range(em-n+1):
            for j in range(em-n+1):
                compare = []
                for ia in range(n): # 이부분이 잘 안나와서 당황했고, 시간을 많이 썼다
                    r = i + ia
                    for ja in range(n):
                        c = j + ja
                        if (e_key[r][c] == 1):
                            compare.append((ia,ja))
                if set(compare) == set(hole): # 마지막에 완벽하게 부분 key와 lock이 일치해야한다
                    return True
                    

        e_key = turn(e_key)
    return False