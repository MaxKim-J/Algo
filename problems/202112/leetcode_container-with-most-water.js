/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  // 맨끝 접근은 좋았다... 그걸 잘 살렸어야 했네
  //! 명징성을 잃지 말자
  let l = 0, r = height.length - 1;
  let maxArea = 0;

  while (l<r) {
      // r-l 인 경우를 고려
      maxArea = Math.max(maxArea, Math.min(height[l], height[r]) * (r-l));
      height[l] < height[r] ? l++ : r--;
  }
  
  return maxArea
};