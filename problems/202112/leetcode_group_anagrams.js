// O(nKlogK) => 변수에 따라서 적절한 시간복잡도를 적시하자, O(NK)
var groupAnagrams = function(strs) {
  // 문자열 배열을 받아서 아나그램끼리 모은다
  // 조건 -> 순서는 상관없다
  // 엣지케이스 -> 배열은 하나 이상의 문자열을 가지고 잇다(하나일때)
  // 엣지케이스 -> 빈문자열이 있는 경우 따로 묶여야함(영어 소문자도 아니고)
  // 길이는 천차만별일 수 있다
  
  // 정렬해서 객체에 저장하고 배열에 모으기 - 배열의 모든 요소를 정렬해야하므로 O(n^2logn) -> 정확히는 O(NKlogK)
  // 빈도 객체, 혹은 map을 만들어서 빈도를 기록 O(n^2) -> key화를 어떻게 해야할까 알파벳 소문자의 비율로 하면 될듯 -> O(NK)
  // 식별 가능한 키로 카테고라이즈화 하기
  
  const anagramMap = {};
  
  for (const str of strs) {
      const anagramId = str.split('').sort().join('');
      if (anagramMap[anagramId]) {
          anagramMap[anagramId].push(str);
      } else {
          anagramMap[anagramId] = [str]; // 이렇게 이차원배열같은 걸 만들면 공간복잡도도 O(n^2)에 가까워진다
      }
  }
  
  return Object.values(anagramMap)
};  

// 정렬한 문자열이 아니라 126개 알파벳 소문자에 대한 문자열(JS에서는 문자열로) 
// 을 key로 삼으면 더 빠르게 O(NK)해결 가능 => 식별 가능한 키를 만들어내는게 중요한 문제였다