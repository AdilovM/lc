/*
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
*/

// Solution


/**
 * @param {number[]} nums
 * @return {number}
 */
//  var findMaxConsecutiveOnes = function(nums) {
//     let left = 0;
//     let right = 0;
//     let countOfZeroes = 0;
//     let globalMax = 0;

//     while(right < nums.length) {

//         if(nums[right] === 0){
//             countOfZeroes += 1;
//         }

//         while(countOfZeroes === 1) {
//             globalMax = Math.max(globalMax, right - left);

//             if(nums[left] === 0) {
//                 countOfZeroes -= 1;
//             }
//             left += 1;
//         }

//         right += 1;
//     }
//     if (countOfZeroes < 1) {
//         globalMax = Math.max(globalMax, right-left)
//     }
//     return globalMax
// };

// let testArr = [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1];
// console.log(findMaxConsecutiveOnes(testArr));
var findMaxConsecutiveOnes = function(nums) {
  let left = 0;
  let right = 0;
  let counterOfOnes = 0;
  while(right < nums.length) {
    if(nums[right] === 0){
      // if current value is 0 shrink the window
      /* whenever we shrink the window we update the global counterOfOnes by picking the largest
      value between current counterOfOnes and current window length AKA distance beween right pointer and left pointer
      */
      counterOfOnes = Math.max(counterOfOnes, right - left);
      left = right + 1;
    };
    // expand the window
    right += 1;
  };
  counterOfOnes = Math.max(counterOfOnes, right - left);
  return counterOfOnes;
};

let testArr = [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1];
console.log(findMaxConsecutiveOnes(testArr));

