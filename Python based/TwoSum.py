# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

###############################Solution#################################
# ###
#  * @param {number[]} nums
#  * @param {number} target
#  * @return {number[]}
# ###
def twoSum(nums, target):
    #1) See Till here Just I have outputted the values that I passed in the function just to verify
    # print(nums)
    # print(target)

    # 2) Step two I will loop through the array thats it
    for num in nums:
        pass
        #Nothing fancy just printing the values of the array thats how I am approaching
        #print(num);
    

    #3) Step three I will loop through all elements of array one after another and will check if it is equal to target
    newArr = []
    i = 0
    j = 0
    for val1 in nums:
        #Nothing fancy just printing the values of the array thats how I am approaching
        for val2 in nums:
            sum = nums[i] + nums[j]
            if (sum == target):
                newArr.append(i)
                newArr.append(j)
                return newArr
            #Incrementing inside loop count
            j = j + 1
        #Incrementing outside loop count
        i = i + 1    
        #console.log(nums[i]);
    print("The final array is : ", newArr)
    #Thats it I got it and now lets return 
    return newArr;
    #############################Function ended here##############################3

arr = [2,7,11,15]
goal = 9

print("The answer is : ", twoSum(arr, goal))