class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        d[0]=-1
        sum,ans=0,0
        for i in range(len(nums)):
            if(nums[i]==0):
                sum-=1
            else:
                sum+=1
            if sum in d:
                ans=max(ans,i-d[sum])
            else:
                d[sum] = i
        return ans
            
        
        
        
