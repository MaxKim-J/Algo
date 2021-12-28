// O(n^2), O(n)
var lengthOfLongestSubstring = function(s) {
  // 중복이 존재하지 않는 형태의 섭스트링중 가장 긴것 => 답에서 이미 중복이 존재하지 않아야 함
  // 투포인터 + 중복이 나오는 경우 답을 저장하고 건너뛰기 => 언제까지? right가 끝에 다다를때까지 
  // 중복이 나오느냐 마느냐는 어떻게 수집할 것이냐 : 객체나 집합 등으로 하지 뭐
  
  // 빈스트링 들어올 수 있음
  // 빈 문자열이 객체의 키값? 상관 x
  
  let left = 0, right = 0;
  let set = new Set();
  let answer = 0;
  
  while(right < s.length) {
      if (set.has(s[right])) { // 이미 나온 경우
          left += 1;
          right = left;
          set = new Set();
          continue;
      }
      
      set.add(s[right])
      answer = Math.max(answer, right - left + 1);
      right += 1;
  }
  
  return answer;
  
};

// 슬라이딩 윈도우 + 발견된 곳 기록하기

var solutions = (s) => {
  const n = s.length;
  const mp = {};
  let answer = 0;

  let i = 0;
  for (let j=0;j<n;j++) {
    // 가장 최근에 발견한 문자의 위치를 저장하는 객체
    if (mp[s[j]] !== undefined) { // 중복을 발견했을때 왼쪽을 끌어올리기
      i = max(mp[s[j]], i) // 왜 Max지 => 현재 i보다는 내려가면 안되긴 함
    }

    // 중복이 없을때는 max하고, 새로 발견한 친구를 mp에 넣기
    answer = max(answer, j - i + 1);
    mp[s[j]] = j+1 // 정확히 말하면 돌아올 인덱스를 저장하게됨
  }

  return answer;
}