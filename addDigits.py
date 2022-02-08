class Solution:
    def addDigits(self, num: int) -> int:
        return 1+(num-1)%9 if num else 0
        
        
# Time complexity - O(1)
# Space complexity - O(1)
