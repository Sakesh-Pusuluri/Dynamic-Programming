# Top down approach

class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo={} # hashmap for memoization
        def dp(n):
            if(n<=1): # base case
                return 0
            if n not in memo:
                memo[n] = min(cost[n-1]+dp(n-1),cost[n-2]+dp(n-2)) # recurrence relation
            return memo[n]
        return dp(len(cost))
        

# Bottom up approach

class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost)<2:
            return 0
        dp = [0]*(len(cost))  # array for storing state variable results
        dp[0]=cost[0] # base case
        dp[1]=cost[1] # base case
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2]) # recurrence relation
        return min(dp[len(cost)-1],dp[len(cost)-2])
    
# Time complexity - O(n)
# Space complexity - O(n)
