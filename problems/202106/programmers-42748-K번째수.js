function solution(array, commands) {
  let answer = [];
  const limit = commands.length
  
  for (let i = 0;i<limit;i++) {
      const [start, end, idx] = commands[i]
      const new_array = array.slice(start-1, end)
      new_array.sort((a,b) => a-b)
      answer.push(new_array[idx-1])
  }
  
  return answer;
}

// sort와 sort(() => {})가 다르다....
// sort는 무조건 문자열로 바꿔서 유니코드로 정렬시킴 그게 숫자라도
// compareFunction이 제공되지 않으면 요소를 문자열로 변환하고 유니 코드 코드 포인트 순서로 문자열을 비교하여 정렬됩니다. 예를 들어 "바나나"는 "체리"앞에옵니다. 숫자 정렬에서는 9가 80보다 앞에 오지만 숫자는 문자열로 변환되기 때문에 "80"은 유니 코드 순서에서 "9"앞에옵니다.