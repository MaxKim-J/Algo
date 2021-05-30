def solution(phone_book):
    answer = True
    hash_map = {}
    
    # 빈도를 먼저 계산한다(in보다 더 빠르게 하기 위해)
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        # 번호 배열을 순회하고 순회하는 번호를 하나씩 뽑아서 temp를 만들고
        # temp가 hash_map에 있는지 확인한다.
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
