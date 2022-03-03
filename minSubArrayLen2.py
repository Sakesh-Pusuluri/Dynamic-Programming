class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arrayLength = len(nums)
        leftPointer,_sum,ans = 0,0,math.inf
        for rightPointer in range(arrayLength):
            _sum +=nums[rightPointer]
            while(_sum>=target and leftPointer<=rightPointer):
                ans = min(ans,rightPointer-leftPointer+1)
                _sum -= nums[leftPointer]
                leftPointer+=1
        if (ans == math.inf):
            return 0   
        return ans
            
# Time complexity -  O(N)
# Space complexity - O(1)
