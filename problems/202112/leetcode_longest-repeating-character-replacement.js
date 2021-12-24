var characterReplacement = function(s, k) {
  const units = new Set(s.split(''));
  let maxLength = 0;
  
  function findMaxRepeatingSubstring (ch, k) {
      let left = 0, right = 0, max = 0;
      
      for (right = 0; right < s.length; right++) {
          if (s[right] !== ch) k--;
          
          while (k < 0 && left < right) {
              if (s[left] !== ch) k++;
              left++;
          }
          
          max = Math.max(right-left+1, max);
      }
      return max;
  }
  
  for (const char of units) {
      maxLength = Math.max(findMaxRepeatingSubstring(char, k), maxLength)
  }
  
  return maxLength;
};