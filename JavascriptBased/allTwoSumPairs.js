// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]


// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

//##############################Solution#################################
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 function twoSum(nums, target) {
    // Step three I will loop through all elements of array one after another and will check if it is equal to target
    let newArr = [];
    // //3) Step three I will make a variable that will store the result when looping through the array
    //This will store the final result
    for (let i = 0; i < nums.length; i++) {
        //Nothing fancy just printing the values of the array thats how I am approaching
        for (let j = i + 1; j < nums.length; j++) {
            let sum = nums[i] + nums[j];
            if (sum == target) {
                newArr.push([i,j]);
            }
        }
        //console.log(nums[i]);
    }
    //console.log("The final array is : ", newArr)
    //Thats it I got it and now lets return 
    return newArr;
};


let arr = [5,4,7,3,2]
let goal = 9

console.log("The answer is : ", twoSum(arr, goal))