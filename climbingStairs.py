# Top down approach

class Solution(object):
    def climbStairs(self, n):
        memo= {} # hashmap for memoization
        def dp(i): 
            # i will be state variable
            if i<=2: # base case
                return i
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2) # recurrence relation
            return memo[i]
        return dp(n) 
    
# Bottom up approach

class Solution(object):
    def climbStairs(self, n):
        dp=[0]*(n+1) # array for storing state variable results
        if n==1:
            return 1
        dp[1] = 1 # base cases
        dp[2] = 2 # base cases
        for i in range(3,n):
            dp[i] = dp[i-1] + dp[i-2] # recurrence relation
        return dp[n] 
      
                
# Time complexity - O(n)
# Space complexity - O(n)
      
                
        
