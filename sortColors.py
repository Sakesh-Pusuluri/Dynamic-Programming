class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,l,h=0,0,len(nums)-1
        while(i<=h):
            if(nums[i]==0):
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            elif(nums[i]==1):
                i+=1
            else:
                nums[i],nums[h]=nums[h],nums[i]
                h-=1
        
        
# Time complexity - O(N)
# Space complexity - O(1)
