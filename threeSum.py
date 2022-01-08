class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if(i==0 or nums[i-1]!=nums[i]):
                def twoSum(nums,i):
                    l=i+1
                    h=len(nums)-1
                    while(l<h):
                        _sum=nums[i]+nums[l]+nums[h]
                        if(_sum<0):
                            l+=1
                        elif(_sum>0):
                            h-=1
                        else:
                            triplets.append([nums[i],nums[l],nums[h]])
                            l+=1
                            h-=1
                            while(l<h and nums[l]==nums[l-1]):
                                l+=1
                twoSum(nums,i)
        return triplets
        
        
# Time complexity - O(N^2)
# Space complexity - O(N)
