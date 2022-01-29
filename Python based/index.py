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

def twoSum(nums, target):
    # print(nums)
    # print(target)

    largerArr=[] #Will store two value array of all possible combinations
    for i in range(0,len(nums)):    
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                #Is tarah c++ mein hoga
                #newArr[0] = i
                #newArr[1] = j
                #Is tarah c++ mein hoga
                #Appending in larger array
                largerArr.append(i)
                largerArr.append(j)
                break
                # I am not returning here I am getting all pairs
                #return newArr
    #Returning larger array that contains all combinations            
    return largerArr            
#Here the main is starting 
target = 9
arr = [5,4,7,3,2]
print("The result is equal to : ",twoSum(arr,target))


