def solution(s):
    answer = 1000
    length = len(s)
    result = ''
    if len(s) == 1:
        return 1
    for l in range(1, (length//2)+1): # 이거 맞추는게 좀 헷갈렸다
        i = 0
        count = 1
        prev = ''
        while i < length + l:
            if (not prev):
                prev = s[i:i+l]
            else:
                if prev == s[i:i+l]:
                    count += 1
                else:
                    result += prev if count == 1 else f'{count}{prev}' # fstring 기억하기
                    prev = s[i:i+l]
                    count = 1 # 1에서 시작해야 했음
            i += l
        answer = min(answer, len(result))
        result = ''
        
    return answer