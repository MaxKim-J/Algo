from copy import deepcopy;

def update(build, order):
    x,y,c,o = order
    
    if (o == 0): #! 처음 구현시 삭제 구현하는 것을 까먹었다
        if build.get((x,y)):
            build[(x,y)].remove(c)
            if (len(build[(x,y)]) == 0):
                del build[(x,y)]
    else:
        if build.get((x,y)):
            build[(x,y)].append(c)
        else:
            build[(x,y)] = [c]


def evaluate(build, order):
    new_build = deepcopy(build)
    x,y,c,o = order
    
    update(new_build, order)
    
    def has_new_build(con, x, y):
        return new_build.get((x, y)) and con in new_build[(x, y)]
        #! get을 고려하지 않아 처음에 Key에러가 났다 => defaultDict의 사용법을 숙지
        # 객체 쓰기에는 자바스크립트가 더 나은듯
    
    # 추가하고 삭제할때마다 전체 아이템을 다 순회해서 조건이 맞는지 전부 확인한다
    for pos, cons in new_build.items():
        x,y = pos
        for con in cons: 
            # 기둥과 보의 조건 중 하나라도 만족하면 존재할 수 있다
            if con == 0:
                confirm = False
                if y == 0:
                    confirm = True
                
                if has_new_build(1, x-1, y) or has_new_build(1, x, y):
                    confirm = True

                if has_new_build(0, x, y-1):
                    confirm = True
                        
                if not confirm:
                    return False
                
            else:
                confirm = False

                if has_new_build(1, x+1, y) and has_new_build(1, x-1, y):
                    confirm = True

                if has_new_build(0, x+1, y-1) or has_new_build(0, x, y-1):
                    confirm = True

                if not confirm:
                    return False
    
    return True
            
def solution(n, build_frame):
    build = {} # 접근 시간을 빠르게 하기 위해 배열을 계속 순회하지 않고 객체로 좌표를 바로 조회할 수 있도록 했음
    for order in build_frame:
        if evaluate(build, order):
            update(build, order)
                
    answer = []
    for pos, cons in build.items():
        for con in cons:
            answer.append([pos[0], pos[1], con])
    
    answer = sorted(answer, key=lambda x:(x[0], x[1], x[2])) # sorted 하면 그대로 배열이 반환된다
            
    return answer