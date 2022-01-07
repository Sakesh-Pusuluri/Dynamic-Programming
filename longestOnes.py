class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count,j,ans=0,0,0
        for i in range(len(nums)):
            if(nums[i]==1):
                count+=1
            while(i-j-count+1>k):
                if(nums[j]==1):
                    count-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans
      
# Time complexity - O(N)
# Space complexity - O(1)
