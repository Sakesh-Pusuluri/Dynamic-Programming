# Top down approach

class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}   # hashmap for memoization
        def dp(i):
            # i will be state variable
            if i==0: # base case
                return 0
            if i<=i<=2: # base case
                return 1
            if i not in memo:
                memo[i]=dp(i-3)+dp(i-2)+dp(i-1) # recurrence relation
            return memo[i]
        return dp(n)
        
 # Bottom up approach

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: # base case
            return 0
        if 1<=n<=2: # base case
            return 1
        dp=[0]*(n+1) # array for storing state variable results
        dp[0],dp[1],dp[2]=0,1,1 # base case
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3] # recurrence relation
        return dp[n]
      
# Time complexity - O(n)
# Space complexity - O(n)
