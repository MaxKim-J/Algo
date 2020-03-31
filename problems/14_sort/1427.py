arr = input()
num_arr = []
for num in arr:
    num_arr.append(int(num))
num_arr.sort(reverse=True)
result = ''
for num in num_arr:
    result += str(num)
print(result)
