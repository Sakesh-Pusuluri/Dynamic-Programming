class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arrayLength = len(nums)
        if(arrayLength<k):
            return 
        leftPointer = 0
        _sum,ans=0,-math.inf
        for rightPointer in range(arrayLength):
            _sum +=nums[rightPointer]
            if(rightPointer-leftPointer+1>=k):
                ans = max(ans,_sum/k)
                _sum-=nums[leftPointer]
                leftPointer += 1
        return ans 
                
            
        
            
# Time complexity - O(N)
# Space complexity - O(1)
        
