
// O(n), O(1)
const productExceptSelf = function(nums) {
    
  // 자기 수 빼고 다른 얘들의 곱으로 정리한 배열 리턴하기 O(n)
  // 입출력 : 배열 정수? 0포함? 

  let zeroCount = 0, mulValue = 1
  for (let i = 0;i<nums.length;i++) {
      if (nums[i] === 0) {
          if (zeroCount == 1) {
              return new Array(nums.length).fill(0)
          }
          zeroCount++;
          continue
      }
      mulValue *= nums[i];
  }

  return zeroCount === 0 ?
    nums.map((num) => mulValue / num)
    : nums.map((num) => num === 0 ? mulValue : 0)
};

// 가장 빨랐던 풀이 O(n), O(n)
// 뒤에서 누적곱을 곱한후 다시 앞에서부터 다시 순회하면서
const productExceptSelf2 = function(nums) {
  // 어..? 이게 더 깔끔해보인다
  var result = new Array(nums.length).fill(1), leftProduct = 1

  result[nums.length-1] = 1

  for(var i = nums.length-2; i >= 0; i--) {
    result[i] = result[i+1] * nums[i+1]
  }
  
  for(i = 0; i < nums.length; i++) {
    result[i] *= leftProduct
    leftProduct *= nums[i]
  }
  
  return result
};