""" 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121] """


class Solution:
    def sortedSquares(self, A):
        squares = []

        for i in A:
            squares.append(i*i)
    
            squares.sort() # sorts squares
        return squares

s=Solution()       
print(s.sortedSquares([-4,-1,0,3,10]))

#Another approach
""" class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A) """
 