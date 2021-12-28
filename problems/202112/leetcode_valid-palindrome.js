var isPalindrome = function(s) {
  // 요구사항 정확히 파악
  // 대문자는 소문자로 바꾸고 알파벳, 숫자가 아닌 문자(공백, 특수문자)는 제외 -> toLowerCase, replace?
  // 그 문자를 팰린드롬인지 검증
  // 특수문자의 범위가 있음? -> 아스키코드 특수문자
  
  s = s.toLowerCase().replace(/[^a-z0-9]+/g, '') //! 부정 문자 그룹 ^ 
  //! 정규표현식 복습하자.. 메타문자, 수량자, 전후방탐색
  
  // 엣지케이스, 케이스 검증
  // 'a' -> true : 문자 하나는 팰린드롬임
  // ' ' -> true : 빈문자열도 팰린드롬
  // 'hello world' -> false
  // 'man! lets go!!' -> false
  
  // 인덱스를 절반을 나눠서 확인해보다가 틀린게 생기는 경우 false
  for (let i = 0;i<Math.floor(s.length / 2);i++) {
      if (s[i] !== s[s.length - 1 - i]) {
          return false
      }
  }
  
  return true
};