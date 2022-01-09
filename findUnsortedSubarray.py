class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        while(low<len(nums)-1 and nums[low]<=nums[low+1]):
            low+=1
        if(low==len(nums)-1):
            return 0
        while(high>0 and nums[high]>=nums[high-1]):
            high-=1
        _max = float('-inf')
        _min=float('inf')
        for val in range(low,high+1):
            _max = max(_max,nums[val])
            _min = min(_min,nums[val])
        while(low>0 and nums[low-1]>_min):
            low-=1
        while(high<len(nums)-1 and nums[high+1]<_max):
            high+=1
        return high-low+1
      
      
      
# Time complexity - O(N)
# Space complexity - O(1)
