function solution(operations) {
  let q = [];
  
  for (let op of operations) {
      if (op === 'D 1') {
          if (q.length === 0) {
              continue
          }
          let idx = -1
          let max = q[0]
          for (let i = 0;i<q.length;i++) {
              if (q[i] >= max) {
                  max = q[i]
                  idx = i
              }
          }
          q.splice(idx, 1)
      } else if (op === 'D -1') {
          if (q.length === 0) {
              continue
          }
          let idx = -1
          let min = q[0]
          for (let i = 0;i<q.length;i++) {
              if (q[i] <= min) {
                  min = q[i]
                  idx = i
              }
          }
          q.splice(idx, 1)
      } else {
          q.push(+op.split(' ')[1])
      }
  }
  
  return q.length === 0 ? [0,0] : [Math.max(...q), Math.min(...q)]
}


// var val = (t[2] === '-' ? Math.min : Math.max)(...list); 
// 이런 구문이 가능하다(신기....) 이걸 사용하면 최대최소를 좀 꿍치는게 가능함
// 그리고 값을 찾았으면 findIndex하면 되는 문제이긴 했음

/*
var val = (t[2] === '-' ? Math.min : Math.max)(...list);
var delIndex = list.findIndex(t=> t ===  val);

list.splice(delIndex, 1);
*/