""" 1572. Matrix Diagonal Sum
Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8 """

class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        #Initializing total sum to 0
        res = 0
        #primary diagonal starts from index 0 of first row
        #secondary diagonal starts from index n-1 of first row
        diag1 = 0
        diag2 = n-1
        #iterating over rows and adding diagonal elements to
        #total sum
        for i in range(n):
            res = res + mat[i][diag1]+mat[i][diag2]
            diag1 += 1
            diag2 -= 1
        if n%2 == 0:   # if matrix size is even 
            return res
        else:
            #In case where matrix is having a center element 
            #we have to subtract it from total sum because 
            #it was added twice earlier
            return res-mat[n//2][n//2]  # return res-mat[1][1] =30-5=25
            
        
        
s=Solution()       
print(s.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))