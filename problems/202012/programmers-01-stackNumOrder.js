// 모예 코테 1

function solution(target) {
  let stack = []
  let num = 1
  while(true) {
    while(num <= target[0]) {
      stack.push(num)
      num++
    }
    if(stack[stack.length - 1] === target[0]) {
      stack.pop()
      target.shift()
      if(target.length === 0) { return true }
    } else {
      return false
    }
  }
}

console.log(solution([3,1,2]))
console.log(solution([3,2,1]))
console.log(solution([3,2,1,5,4,8,7,6]))