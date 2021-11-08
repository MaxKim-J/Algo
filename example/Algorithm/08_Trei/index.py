class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
      cur_node = self.root
      for c in s: 
          if c not in cur_node:
              cur_node[c] = {}
          cur_node = cur_node[c]
      cur_node["*"] = s # 끝 노드에 완성된 노드

    def search(self, s):
      cur_node = self.root
      for c in s:
          if c in s:
              cur_node = cur_node[c]
          else:
              return False
      return "*" in cur_node