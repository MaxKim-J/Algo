# 백준  5397: 키로거
# https://www.acmicpc.net/problem/5397
# 시간 : 40분
# 경과 : 런타임 에러 -> 못품
#! 동빈나 수업 문제

test_case = int(input())
for _ in range(test_case):
    left_stack, right_stack = [], []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

#! 싸해지는 포인트를 좀 잘 잡아야될거같음. 그러면 니는 틀린거임..(잘못 접근)
#! => 모든 조건을 다 그렇게 처리하가에는 너무 힘이 들때라던지
#! 코드 치는 시간 그리 길지 않으니 생각 충분히 하기 -> 확실히 컨셉을 잡고 가기
