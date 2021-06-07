def solution(p):
    a = [0] * len(p)
    end = len(p)
    
    for i in range(end):
        count = 0
        for j in range(i+1, end):
            count += 1
            if p[j] < p[i]:
                break
        a[i] = count
        
    return a