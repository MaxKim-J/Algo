# 트리
2020.01.25

## 정의
트리는 부모 자식관계에 따라 노드를 에지로 연결한 자료구조  
그래프이기도 함 + 사이클이 없는 그래프 = 트리에서 두 노드의 경로는 유일하게 하나  
두 노드를 연결하는 에지들을 순서대로 나열한 것으로 길이는 경로의 에지 개수로 정의함  

## 특징
- 그래프의 한 종류, 최소 연결 트리라고보 불림
- 트리는 계층모델이다
- 트리는 DAG의 한 종류 - loop, circuit없음
- 노드가 n개인 트리는 항상 n-1개의 에지를 가진다
- 한 개의 루트 노드만이 존재하며 모든 자식 노드는 한개의 부모 모드만을 가진다

## 이진트리 

### 정의
자식노드가 최대 2개뿐인 트리를 이진트리라고 함  
두개의 자식 = 왼쪽 오른쪽
```python
class Node:
  def __init__(self, key, parent=None, left=None, right=None):
    self.key = key
		self.parent = parent
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.key)

class Tree:
	def __init__(self):
		self.root = None
		self.size = 0
```

### 순회
트리의 각 노드를 어떤 순서에 따라 빠짐없이 방문하면서 노드의 정보를 출력, 수정 하는 것, 재귀를 이용해서 코드 작성함
1. preorder : MLR
2. inorder : LMR
3. postorder : LRM
```python
def preorder(self, v): # 노드 v와 자손 노드를 preorder로 방문하면서 출력
	if v != None:
		print(v.key)
		self.preorder(v.left)
		self.preorder(v.right)

def inorder(self, v): # 노드 v와 자손 노드를 preorder로 방문하면서 출력
	if v != None:
		self.preorder(v.left)
		print(v.key)
		self.preorder(v.right)

def postorder(self,v):
  if v != None:
		self.preorder(v.left)
		self.preorder(v.right)
    print(v.key)
```