// preOrder, postOrder, inOrder
// 모두 DFS의 한 방법 => 일단 순서대로 있으면 하나만 끝으로 내려간다
// 없으면 그 다음 순서로 감
//! DFS니까 리프까지 탐색을 하고나면 다시 위로 올라와 방문했던 곳에서 또 다른 방문하지 않은 자식노드를 바라본다
//! 그게 다 visited가 된 경우는 또 올라감
//!! 스택이 무엇인지를 특히 더 상기해야한다. 왜 거까지 내려가냐?
// 왼쪽과 오른쪽은 탐색, 방문은 나 하나

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor () {
    this.root = null
  }
  insert(value) {
    let newNode = new Node(value);
    if(this.root == null) {
      this.root = newNode;
      return this
    }
    let current = this.root;
    while(true){
      if(value === current.value) return undefined;
      if(value < current.value) {
        if(current.left === null) {
          // 리프의 제자리에 삽입하고 BST를 리턴
          current.left = newNode;
          return this
        }
        current = current.left
      } else {
        if(current.right === null) {
          current.right = newNode;
          return this;
        }
        current = current.right
      }
    }
  }
  // preOrder (나 -> 왼 -> 오)
  // 일반적으로 생각할 수 있는 DFS에 가깝다
  DFSPreOrder() {
    const data = [];
    const traverse = (node) => {
      // 일단은 자식으로 내려간 것에 대해서는 무조건 방문을 한다
      data.push(node.value)
      // 그리고 왼쪽과 오른쪽을 봄
      // 일단 왼쪽을 보고 왼쪽 방문 후에 또 리프를 만나면 다시 위로 올라와 오른쪽을 본다(그제서야 콜스택에서 제거되기 때문에)
      if(node.left) traverse(node.left);
      if(node.right) traverse(node.right);
    }
    traverse(this.root)
    return data
  }
  // postOrder(왼-> 오-> 나)
  // DFS처럼 리프인 경우에 다시 돌아간다는 것에 중점을 둔다. 일단 방문하지않고 내려간다(자식이 있으면)
  // 방문은 거의 밑부터 다시 위로 올라가는 식으로 이뤄짐
  DFSPostOrder() {
    const data = [];
    const traverse = (node) => {
      if(node.left) traverse(node.left);
      if(node.right) traverse(node.right);
      data.push(node.value)
    }
    traverse(this.root)
    return data
  }
  // inOrder (왼 -> 나 -> 오)
  // 트리의 왼쪽부터 그림의 순서대로 방문한다는 특징이 있다
  // 왼쪽은 일단 계속 내려가고, 오른쪽을 찾기 전에 방문을 한다
  DFSInOrder() {
    const data = [];
    const traverse = (node) => {
      node.left && traverse(node.left);
      data.push(node.value)
      node.right && traverse(node.right);
    }
    traverse(this.root)
    return data
  }
}

const BST = new BinarySearchTree()

BST.insert(10)
BST.insert(6)
BST.insert(3)
BST.insert(8)
BST.insert(15)
BST.insert(20)

console.log(BST.DFSPreOrder())
console.log(BST.DFSPostOrder())
console.log(BST.DFSInOrder())


