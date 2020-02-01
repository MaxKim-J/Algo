# 데크
2020.01.19
큐 스택 말고 데크만 정리

## 정의
데크는 스택과 큐 자료구조를 혼합한 자료구조  
선입선출도 되고 후입선출도 되고...  
데크는 스택과 큐를 동시에 구현하는데 사용

## Collections 패키지
파이썬으로 푸는 알고리즘 문제에서  
데크를 굳이 클래스로 구현할 필요는 0에 수렴(느리다)  
사실 스택이나 큐도 마찬가지다(데크가 둘다 커버함)
```python
from collections import deque

dq = deque('data')
for elem in dq:
  print(elem.upper(), end='')
dq.append('r') # 뒤추가
dq.appendleft('k') # 앞추가
dq.pop() #뒤 삭제
dq.popleft() #앞 삭제
dq.extend('structure') #여러 항목 뒤에 삽입
dq.extendleft(reversed('python')) #여러 항목 앞에 삽입
```

## reference
- 양성봉, [파이썬과 함께하는 자료구조의 이해](http://www.yes24.com/Product/Goods/57949931?scode=032&OzSrank=1)