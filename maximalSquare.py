
# Bottom up approach

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans=0
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)] # array for storing state variable results
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                if(matrix[i-1][j-1]=='0'):
                    dp[i][j]=0 # recurrence relation
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1] ,dp[i][j-1], dp[i-1][j]) # recurrence relation
                ans = max(ans,dp[i][j]**2)
        return ans
                

# Time complexity - O(mn)
# Space complexity - O(mn)
