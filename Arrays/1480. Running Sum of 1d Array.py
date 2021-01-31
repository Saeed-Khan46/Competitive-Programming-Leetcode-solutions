""" 
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17] """

class Solution():
    def runningSum(self, nums):
        
        mysum = 0
        for i in range(0,len(nums)):
            nums[i] = nums[i] + mysum 
            mysum  = nums[i]

        return nums

            
            

s=Solution()       
print(s.runningSum([1,2,3,4]))
