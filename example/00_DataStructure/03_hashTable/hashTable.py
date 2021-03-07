'''
해쉬 테이블

데이터를 효율적으로 관리하기 위해 임의의 길이 데이터를 고정된 길이의 데이터를 매핑하는 것
해시함수를 구현하여 데이터 값을 해시 값으로 바꾼다
메모리 등의 검색 효율을 높이기 위해서 사용. 뒤지지 않고 해쉬함수 결과값을 알 수 있다면 빠르게 데이터에 접근 가능
하드디스크나 클라우드에 존재하는 무한에 가깝게 많은 데이터들을 유한한 개수의 해시값으로 매핑하면 작은 메로리로도 프로세스 관리와 검색이 가능해짐

괜찮은 해쉬함수 : 빨라야함, 충돌이 적어야함, 결정적이어야 함
충돌 문제 : 해시 테이블 내의 데이터가 많아지면 상이한 데이터가 같은 해시값을 가지고 있어서 충돌이 나는 현상이 발생
충돌 해결 방법
  1. Open Addressing : 충돌한 데이터를 다른 빈칸으로 이동시킴 - 선형 탐색(linear probing)
  2. chaining : 해쉬 테이블 한칸을 연결리스트로 만들어 노드를 계속 추가하는 방식. 충돌이 절대 발생하지 않으나 메모리가 많이 필요하고 탐색에 시간이 걸릴 수 있음
'''

# Open Addressing Hash Table

# 일차원배열에 entries한 것처럼 [key, value] 이렇게 저장되어 있음
hash_table = list([0 for i in range(8)])

# 키를 해싱
def hash_function(key):
    return hash(key) % 8

def save_data(key, value):
    hash_address = hash_function(key)
    # 키가 이미 존재한다면 그 옆의 칸부터 끝가지 탐색하기 시작하여 넣을 곳을 찾음
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            # 없다면 값 저장
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            # 이미 키가 있다면 값 수정
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
    # 키가 존재하지 않는다면 그냥 거기다가 넣음
    else:
        hash_table[hash_address] = [key, value]

def read_data(key):
    hash_address = hash_function(key)
    # 다음칸 탐색해서 빈칸에 넣기
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == key:
                return hash_table[index][1]
    else:
        return None


# Chaining Hash Table
hash_table = list([0 for i in range(8)])

def hash_function(key):
    return hash(key) % 8

def save_data(key, value):
    hash_address = hash_function(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([key, value])
    else:
        hash_table[hash_address] = [[key, value]]
    
def read_data(key):
    hash_address = hash_function(key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None