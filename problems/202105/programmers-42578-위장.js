// 경우의 수를 단순하게 생각하기

function solution(clothes) {
  let answer = 1;
  let obj={};
  
  // 빈도를 구하는데, 이때 곱경우를 구하기 좋게 안입는 경우의 수도 같이 곱해줌
  for(let i=0; i<clothes.length; i++){
      obj[clothes[i][1]]=(obj[clothes[i][1]] || 1) + 1;
  }
  
  // 객체에 있는 모든 값을 곱해주고
  for(let key in obj){
      answer *= obj[key];
  }
  
  // 모두 옷을 입지 않는 경우 하나를 빼줌
  return answer-1;
}