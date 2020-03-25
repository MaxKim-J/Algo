# 백준 2775 : 부녀회장이 될테야 풀이 
# https://www.acmicpc.net/problem/2869
# 시간 : 1시간 - 못품
# 경과 : 시간초과 

#! 재귀함수로 풀면 시간초과;;
"""
def people_in_room(floor, room):
    if floor == 0:
        return room
    floor -= 1
    rooms = range(room+1)
    result = 0
    for room in rooms:
        result += people_in_room(floor, room)
    return result

data_num = int(input());
for _ in range(data_num):
    floor = int(input())
    room = int(input())
    print(people_in_room(floor, room))
"""

# 거의 dp에 가까운 방법
# 이것도 일일히 밑에층부터 해보긴 하는데, 기본적인 0층 배열을 가지고 위층 배열을
# 일차원적으로 계속 만들어낸다
# 방 호수를 배열의 끝으로 잡는다(이건 나도 접근 잘 한듯)
data_num = int(input())
for _ in range(data_num):
    floor = int(input())
    room = int(input())
    people = [ i for i in range(1, room+1)]
    for _ in range(floor):
        for j in range(1,room):
            people[j] += people[j-1]
    print(people[-1])

#! 못푼 이유1) : 재귀로 풀면 느릴 것을 예상하지 못해서
#* 재귀는 기본적으로 느리니까 dp할수 있으면 한다

#! 못푼 이유2) : 배열로 풀려면 2차원배열로 값을 다 가지고 있어야 한다고 생각해서
#* 필요한 값만 가지고 있어도 되고 쓰면 없애도 되고 
