N,M = map(int,input().split())

if N==1 or M==1 :
    result = 1
elif M in (2,3) :
    if N >= 3 : 
      result = M
    else : 
      result = (M+1)//2
elif M in (4,5,6) :
    if N >= 3 : 
      result = 4
    else : 
      result = (M+1)//2
elif M >= 7 :
    if N >= 3 : 
      result = (M-6) + 4
    else : 
      result = 4

print(result)