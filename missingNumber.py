class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = len(nums)*(len(nums)+1)//2
        actualSum = sum(nums)
        return expectedSum-actualSum
        
        
# Time complexity - O(N)
# Space complexity - O(1)
