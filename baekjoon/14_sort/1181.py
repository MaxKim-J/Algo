# 백준 1181번 단어정렬

# test_num = 13
# test_arr = ['but', 'i', 'wont', 'hesitate', 'no', 'more',
#             'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

num = int(input())

arr = []
for _ in range(num):
    figure = input()
    arr.append(figure)

len_dict = {}
for elem in arr:
    try:
        if (len_dict[len(elem)]) and (elem not in len_dict[len(elem)]):
            len_dict[len(elem)].append(elem)
    except KeyError:
        len_dict[len(elem)] = [elem]

for arr in sorted(len_dict.items()):
    for elem in sorted(arr[1]):
        print(elem)

# voca_list = []
# for i in range(int(input())):
#     voca_list.append(input())

#! 리스트 중복을 이런식으로 제거했다
# set_voca_list = list(set(voca_list))

# sort_voca_list = []
# for j in set_voca_list:
#     sort_voca_list.append((len(j), j))

#! 시퀀스 원소의 정렬은 앞을 먼저 정렬한 후 뒤를 정렬한다(?!)
# sort_voca_list.sort()
# for len_voca, voca in sort_voca_list:
#     print(voca)
