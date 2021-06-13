function solution(N) {
  const answer = N.map(c=> c + '').
          sort((a,b) => (b+a) - (a+b)).join('');
  return answer[0] === '0' ? '0' : answer;
}

// 아직 js sort를 제대로 이해하고 있지 못하다...