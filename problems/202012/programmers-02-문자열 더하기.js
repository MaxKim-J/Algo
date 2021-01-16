// 모예 코테 2

function solution(a,b) {
  const minLength = Math.min(a.length, b.length)
  const aArr = a.split('').reverse()
  const bArr = b.split('').reverse()
  let carriage = 0
  let answer = []

  let i = 0
  for(;i < minLength; i++) {
    let result = parseInt(aArr[i]) + parseInt(bArr[i]) + carriage
    if(result >= 10) {
      result -= 10
      carriage = 1
    } else {
      carriage = 0
    }
    answer.unshift(result)
  }
  const longArr = aArr.length >= bArr.length ? aArr:bArr
  return `${parseInt(longArr.slice(i).join('')) + carriage}${answer.join('')}`
}

// 최대 몇자라고 안 나왔던 것 같음
console.log(solution('199','2555'))
console.log(solution('100','2555'))
console.log(solution('3248723948792837598798','35729835798375982738342344398'))