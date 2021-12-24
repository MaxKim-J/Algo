// O(nlogn), O(n)
var isAnagram = function(s, t) {
  // 애너그램
  
  // 엣지케이스 - s,t는 모두 1일수도 있음
  // 빈도를 모두 체크한후, 다른 문자열 순회하면서 이질적인 문자가 있을 때 false 리턴
  // 유니코드 정렬한 후 둘이 일치하면 애너그램인것
  
  return s.split('').sort().join('') === t.split('').sort().join('');
};

// O(n), O(n)
var isAnagram = function(s, t) {
  // 둘이 길이 다를수도 있음
  if(s.length !== t.length) return false;
  
  const freqMap = {};
  for (let i = 0;i<s.length;i++) {
      if (freqMap[s[i]] === undefined) {
          freqMap[s[i]] = 1;
      } else {
          freqMap[s[i]] += 1;
      }
  }

  for (let i = 0;i<t.length;i++) {
      if (!freqMap[t[i]]) return false
      freqMap[t[i]] -= 1 // 빈도를 계속 빼다가, unefined가 나오거나 0이 나오면 애너그램 아님
  }
  
  return true
};