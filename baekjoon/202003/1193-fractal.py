# 백준 1193번

def chunk_valid(num):
    chunk_first, chunk_num= 1,1
    while chunk_first + chunk_num <= num:
        chunk_first += chunk_num
        chunk_num += 1
    return chunk_num, num-chunk_first

def chunk_cal(chunk, order):
    if chunk % 2 == 0:
        left, right = 1, chunk
        for _ in range(order):
            left += 1
            right -= 1
    else:
        left, right = chunk, 1
        for _ in range(order):
            left -= 1
            right += 1

    return f"{left}/{right}"
    
N = int(input())
chunk_result = chunk_valid(N)
print(chunk_cal(chunk_result[0], chunk_result[1]))