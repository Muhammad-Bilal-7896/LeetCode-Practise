#two sum algorithm for all pair possible 
#This is not asked in leetcode but Amin this was your question 
# right not the problem statement in leetcode.And also not acceptable in 
# leet code because leetcode statement is different

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
                largerArr.append([i,j])
                # I am not returning here I am getting all pairs
                #return newArr
    #Returning larger array that contains all combinations            
    return largerArr            
#Here the main is starting 
target = 9
arr = [5,4,7,3,2]
print("The result is equal to : ",twoSum(arr,target))


