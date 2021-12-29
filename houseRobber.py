# Top down approach

class Solution(object):
    def rob(self, nums):
        memo={} # hash map for memoization
        def dp(i):
            # i will be state variable 
            if i==0: # base case
                return nums[0]
            if i==1 :  # base case
                return max(nums[0],nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1),dp(i-2)+nums[i])  # recurrence relation
            return memo[i]
        return dp(len(nums)-1)

# Botton up approach

class Solution(object):
    def rob(self, nums):
        if len(nums)-1 == 0:
            return nums[0]
        dp=[0]*(len(nums)) # array for storing state variable results
        dp[0] = nums[0] # base case
        dp[1] = max(nums[0],nums[1]) # base case
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i]) # recurrence relation
        return dp[len(nums)-1]
      
# Time complexity - O(n)
# Space complexity - O(n)
