class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            while(l<h):
                _sum = nums[i]+nums[l]+nums[h]
                if(_sum<target):
                    count+=h-l
                    l+=1
                else:
                    h-=1
        return count
      
      
      
# Time complexity - O(N^2)
# Space complexity - O(N)
