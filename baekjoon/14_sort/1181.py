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
