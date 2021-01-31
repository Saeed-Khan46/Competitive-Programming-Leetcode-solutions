""" 1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


Example 3:

Input: nums = [1,2,3]
Output: 0
 """


class Solution:
    def numIdenticalPairs(self, nums):

        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

s=Solution()       
print(s.numIdenticalPairs([1,2,3,1,1,3]))        

# optimised solution

# class Solution:
#     def numIdenticalPairs(self, nums):
#         ans = 0
#         d = {}
#         for num in nums:
#             if num in d:
#                 ans = ans + d[num]
#                 d[num] = d[num] + 1
#             else:
#                 d[num] = 1
#         return ans

# s=Solution()       
# print(s.numIdenticalPairs([1,2,3,1,1,3]))
