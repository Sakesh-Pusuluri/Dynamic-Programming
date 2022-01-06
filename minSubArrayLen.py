class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum,j,ans=0,0,float('inf')
        for i in range(len(nums)):
            _sum+=nums[i]
            while(_sum>=target):
                ans=min(ans,i-j+1)
                _sum-=nums[j]
                j+=1
        if ans==float('inf'):
            return 0
        return ans
      
# Time complexity - O(n)

# Space complexity - O(1)
        
