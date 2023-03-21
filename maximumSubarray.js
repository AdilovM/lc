/*
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum possible for ‘k’ consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700
*/


const maxSubarray = (array, k) => {
  for(let i = 0; i < array.length - k + 1; i++){
    let currentSum = 0;
    for(let j = 0; j < k; j++){
      currentSum = currentSum + arrayy[i + j];
    }
    maxSum = max()
  }
}