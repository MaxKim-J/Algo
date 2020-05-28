# 백준 2981: 검문
# https://www.acmicpc.net/problem/2981
# 시간 : 못품
# 경과 : 못품
#! 복습필수

# 최대공약수를 빠르게 구해주는 유클리드 호제법


def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

# 약수 리스트를 구해주는 함수


def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list


# 입력함수
N = int(input())
freight = []
for _ in range(N):
    freight.append(int(input()))
freight.sort(reverse=True)

# 화물들의 차이 입력
freight_diff = []
for i in range(len(freight)-1):
    freight_diff.append(freight[i] - freight[i+1])

# 화물들의 차이를 최대공약수 함수를 이용해 구해주기
if len(freight_diff) == 1:
    answer = freight_diff[0]
elif len(freight_diff) == 2:
    answer = gcd(freight_diff[0], freight_diff[1])
else:
    answer = freight_diff[0]
    for i in range(1, len(freight_diff)):
        answer = gcd(answer, freight_diff[i])

# 구한 최대공약수의 모든 약수 출력
for i in div(answer):
    print(i, end=' ')

"""
임의의 두 수 X0와 X1 (X0 < X1)이 있다. 이때 X0와 X1는 gcd (gcd>=2)를 갖고 있다고 할 때 X0와 X1은 각각 다음과 같이 표현이 가능하다.

X0 = a * gcd
X1 = b * gcd
따라서 X1 - X0 = (b - a) * gcd 가 되고, 이것은 (X1 - X0)가 gcd의 배수임을 의미한다.

마찬가지로 임의의 두 수 X0와 X1 (X0 < X1)이 특정한 수로 나눴을 때 같은 나머지를 가지고 있을 때 다음과 같이 표현이 가능하다. (t는 임의의 정수)

X0 = a * t + r
X1 = b * t + r
X1 - X0 = (b - a) * t

위에서 (X1 - X0)가 gcd의 배수임을 의미했기 때문에 t도 gcd의 배수 혹은 약수일 것이다.
나머지가 같은 수의 집합체는 큰 수부터 정렬했을 때, 두 수의 차이가 일정하다는 뜻이다.

즉 다시 말해 a, b, c, d(a>b>c>d)의 나머지가 같은 수를 구하고자 할 때는
a-b, b-c, c-d 의 최대공약수를 구하면 된다. 그리고 답은 그 최대공약수의 약수
"""

"""
# 다른풀이 더 직관적

A=a*M+r
B=b*M+r

큰수에서 작은수를 빼주면 나머지가 제거되는것을 알수있고
A-B=(a-b)*M 두 수를 빼서 나오는 숫자의 약수에 M이 포함되있는것을 확인할 수 있다.
그렇다면 문제를 해결하기위해 주어진수중 큰수에서 작은수를 빼고 M의 후보군을 구한후
각 수에 M후보군을 하나씩 나눠 나머지가 같은지 보면 될것이다.

import math
 
N=int(input())
num_list=[]

# A-B를 통해 m구하기

while N>0:
    N-=1
    num_list.append(int(input()))

# 그냥 두수를 뽑은거구나 => 이값이 A-B
if num_list[0]<num_list[1]:
    m=num_list[1]-num_list[0]
else:
    m=num_list[0]-num_list[1]


# 약수구하기 => A-B의 약수 다 구하기
# m은 A-B의 약수임이 확실하고, 모든 수의 차에서 똑같이 나타나야 함
# 여기서 M은 모든수를 나눴을때 같은 나머지를 남기게 하는 수
#! 가능한 M들 => m의 약수 : a-b와 M을 곱하면 무조건 그 수가 나와야 함, a-b와 M은 A-B의 약수로 둘이 곱하면 A-B가 나오구
# 그러므로 m의 약수를 모조리 구해준다

m_candidate=[m]
for i in range(2,int(math.sqrt(m))+1):
    if m%i==0:
        m_candidate.append(i)
        m_candidate.append(m//i)
 
# m의 약수들로 루프를 돌려서 입력받은 모든 숫자를 나누고 나머지가 같은 것들을 리스트에 넣는다
M=[]
for i in range(len(m_candidate)):
    r=num_list[0]%m_candidate[i]#나머지 구하기
    for j in range(1,len(num_list)):
        #나머지 같은지 확인
        if r!=num_list[j]%m_candidate[i]:#나머지가 다르면 패스
            break
        if j==len(num_list)-1:#모든 나머지가 같으면 m추가
            M.append(m_candidate[i])
 
M.sort()
 

for k in M:#모든 M 출력
    print(k,end=' ')
"""
