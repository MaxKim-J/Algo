from itertools import combinations

def solution(orders, course):
    tree = [{} for i in range(max(course)+1)]
    max_values = {k:0 for k in course}
    
    for o in orders:        
        for c in course:
            cs = list(combinations(list(o), c))
            for i in cs:
                # 여기서 차라리 처음부터 정렬된 문자열로 바꾸기
                key = ''.join(list(sorted(list(i))))
                if tree[c].get(key):
                    tree[c][key] += 1
                    if (tree[c][key] > max_values[c]):
                        max_values[c] = tree[c][key]
                else:
                    tree[c][key] = 1

    answer = []
    for c in course:
        for key, value in tree[c].items():
            if (value == max_values[c]):
                answer.append(key)
    
    return list(sorted(answer))