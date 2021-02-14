class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// 값을 평가해서 타고 내려간다는 점이 중요
class BinarySearchTree {
  constructor() {
    this.root = null
  }

  insert(value) {
    const newNode = new Node(value);
    if(this.root === null) {
      this.root = newNode
      return this
    }
    let current = this.root;
    while(true) {
      if(value === current.value) return undefined
      if(value < current.value) {
        if(current.left === null) {
          current.left = newNode;
          return this
        }
        current = current.left
      } else {
        if(current.right === null) {
          current.right = newNode;
          return this
        }
        current = current.right
      }
    }
  }

  find(value) {
    if(this.root === null) return false
    let current = this.root
    let found = false
    // current가 null일 경우이거나 찾았을 경우 빠져나옴
    while(current && !found) {
      if(value < current.value) {
        current = current.left
      } else if (value > current.value) {
        current = current.right
      } else {
        found = true
      }
    }
    if(!found) return undefined
    return current
  }

  // 기억하기 쉽게 delete by copying
  delete(value) {
    if(this.root === null) return false
    let current = this.root
    let parent = null
    let direction = null
    while(current) {
      parent = current
      if(value < current.value) {
        current = current.left
        // 마지막 방향을 저장
        direction = 'left'
      } else if (value > current.value) {
        current = current.right
        // 마지막 방향을 저장
        direction = 'right'
      } else {
        // 맞는걸 찾았을때, 혹은 current가 Null일때 빠져나옴
        break
      }
    }
    // 없으면 삭제할 수 없음
    if(current === null) {return false}
    
    let copyTarget = null
    let targetParent = null
    // 왼쪽노드가 있을 때 : 왼쪽노드에서 가장 큰 값을 찾아 삭제할 노드에 키값 복사
    if(current.left) {
      copyTarget = current.right
      while(copyTarget.right) {
        targetParent = copyTarget
        copyTarget = copyTarget.right
      }
      targetParent.right = null
    // 왼쪽노드가 없을 때 : 오른쪽 노드에서 가장 작은값을 찾아 삭제할 노드에 키값 복사
    } else if (current.right) {
      copyTarget = current.left
      while(copyTarget.left) {
        targetParent = copyTarget
        copyTarget = copyTarget.left
      }
      targetParent.left = null
    }
    // 카피할 노드의 왼쪽 오른쪽을 기존 노드의 왼쪽 오른쪽으로 채움
    copyTarget.left = current.left
    copyTarget.right = current.right

    // 루트 노드를 삭제하는 경우
    if(this.root === current) {
      // 자식노드가 있으면 => copyTarget을 루트로 복사
      if(copyTarget) {
        this.root = copyTarget
      // 없으면 => 트리를 비움
      } else {
        this.root = null
      }
    // 아닌 경우 => 복사를 수행함
    } else {
      parent[direction] = copyTarget
    }
  }
}