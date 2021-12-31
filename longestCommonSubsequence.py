# Top down approach

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        memo=[[-1]*(n+1) for _ in range(m+1)] # memoization
        def dp(i,j):
            if(i==len(text1) or j == len(text2)): # base case
                return 0
            if(text1[i]==text2[j]):
                memo[i][j] = 1 + dp(i+1,j+1) # recurrence relation
            else:
                memo[i][j] = max(dp(i,j+1),dp(i+1,j)) # recurrence relation
            return memo[i][j]
        return dp(0,0)
        
        
# Bottom up approach

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1),len(text2) 
        dp=[[0]*(n+1) for _ in range(m+1)]  # array for storing state variable results 
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1] # recurrence relation
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) # recurrence relation
        return dp[m][n]
        

# Time complexity - O(mn)
# Space complexity - O(mn)
