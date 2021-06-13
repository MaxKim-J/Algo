function solution(C) {
  C.sort((a,b) => b - a)    
  for (let i = C[0];i>-1;i--) {
      const count = C.filter((v) => v >= i).length
      if (count >= i) {
          return i
      }
  }
}