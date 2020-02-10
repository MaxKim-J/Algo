# 10814 나이순 정렬

data_num = int(input())
arr = []
for _ in range(data_num):
    person = input().split()
    person[0] = int(person[0])
    arr.append(person)

age_dict = {}
for member in arr:
    try:
        age_dict[member[0]].append(member[1])
    except KeyError:
        age_dict[member[0]] = [member[1]]

for mem in sorted(age_dict.items()):
    for who in mem[1]:
        print(f"{mem[0]} {who}")

# 사실 딕셔너리 안쓰고도 짜피 리스트 순서는 정해졌으니 이렇게 해도 된다

# import sys
# n = int(sys.stdin.readline())
# member = []
# for i in range(n):
#     member.append(list(sys.stdin.readline().split()))
#! member.sort(key=lambda x: int(x[0])) sort는 안정정렬
# for i in range(n):
#     print(member[i][0], member[i][1])
