'''
연결리스트

배열은 순차적으로 연결된 공간에 데이터를 나열하는 구조인데
연결리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

삽입 삭제는 연결리스트가, 탐색은 그냥 리스트가 유리하다 => 물론 탐색이 필요한 삭제는 별로
미리 데이터공간을 할당하지 않아도 된다(그냥 리스트는 미리 할당해하고 삽입 삭제가 일어나면 shift가 필요)
'''

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
  
  def add(self, data):
    if not self.head:
      self.head = Node(data)
    else:
      node = self.head
      # 끝까지 탐색
      while node.next:
        node = node.next
      node.next = Node(data)

  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

  def delete(self, data):
    if not self.head:
      print("리스트에 노드가 없습니다")
      return
    
    if self.head.data == data:
      self.head = self.head.next
    else:
      node = self.head
      while node.next:
        if node.next.data == data:
          node.next = node.next.next
          return
        else:
          node = node.next
      print('삭제하려는 노드가 리스트에 없습니다')
  
  def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


linked_list = LinkedList(0)
linked_list.desc()

for i in range(1, 10):
  linked_list.add(i)
linked_list.desc()

for j in range(5, 11):
  linked_list.delete(j)

linked_list.desc()
