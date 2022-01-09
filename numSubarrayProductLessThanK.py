class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod = 1
        ans,i=0,0
        for j in range(len(nums)):
            prod*= nums[j]
            while(prod>=k and i <len(nums)):
                prod/=nums[i]
                i+=1
            ans+=j-i+1
        return ans
     
    
    
# Time complexity - O(N)
# Space complexity - O(1)
