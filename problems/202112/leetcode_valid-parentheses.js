/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  // 괄호 매칭시키기
  
  // 엣지케이스 -> length === 1인경우 : 짝이 맞지 않음
  if (s.length === 1) return false
  
  // 스택을 이용한 풀이 => O(n)
  // 순서가 맞지 않는 경우 false가 나와야 하나? 개수만 맞으면 되는건가? valid의 기준
  // 맨 앞에 스택에 넣을 수 없는 것이 오는 경우
  
  const stack = [];
  const match = {
      '(':')',
      '{':'}',
      '[':']'
  }
  for (let i = 0;i<s.length;i++) {
      // 순회하면서 괄호 여는거 발견했을 때 stack에 넣기
      if ('([{'.includes(s[i])) {
          stack.push(s[i])
      } else {
          const last = stack[stack.length - 1]
          if (match[last] === s[i]) {
              stack.pop()
          } else {
              return false
          }
      }
      
  }
      
  // 마지막까지 진행했을 때 stack이
  return stack.length === 0;
  
};