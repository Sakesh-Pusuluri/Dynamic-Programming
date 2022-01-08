class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest=float('inf')
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            while(l<h):
                _sum = nums[i]+nums[l]+nums[h]
                target_diff = target-_sum
                if(_sum==target):
                    return target-target_diff
                if(abs(target_diff)<abs(smallest)) or ((abs(target_diff) == abs(smallest) and target_diff > smallest)):
                    smallest = target_diff 
                if(target_diff>0):
                    l+=1
                else:
                    h-=1
        return target-smallest

      
# Time complexity - O(N^2)
# Space complexity - O(N)
