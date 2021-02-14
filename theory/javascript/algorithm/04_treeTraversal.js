// 트리 순회 - BFS, DFS 

// Binary Search Tree
const treeSample = {
  a: {left: 'b', right: 'c'},
  b: {left: 'd', right: 'e'},
  c: {left: null, right: 'g'},
  d: {left: null, right: null},
  e: {left: 'f', right: null},
  f: {left: null, right: null},
  g: {left: null, right: null},
}

// BFS - 큐
function BFS(tree, root) {
  const visited = []
  const queue = []
  let node = root
  queue.push(root)

  while(queue.length) {
    // 앞을 뺌
    node = queue.shift()
    visited.push(node)
    if(tree[node].left !== null) {
      // 뒤에 넣음
      queue.push(tree[node].left)
    }
    if(tree[node].right !== null) {
      // 뒤에 넣음
      queue.push(tree[node].right)
    }
  }

  return visited
}

console.log(BFS({...treeSample}, 'a'))

// DFS - 스택
function DFS(tree, root) {
  const visited = []
  const stack = []
  let node = root
  stack.push(root)

  while(stack.length) {
    // 뒤를 뺌
    node = stack.pop()
    visited.push(node)
    if(tree[node].left !== null) {
      // 뒤에 넣음
      stack.push(tree[node].left)
    }
    if(tree[node].right !== null) {
      // 뒤에 넣음
      stack.push(tree[node].right)
    }
  }

  return visited
}

console.log(DFS({...treeSample}, 'a'))

