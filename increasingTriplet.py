class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstLargest = float('inf')
        secondLargest = float('inf')
        for i in nums:
            if(i<=firstLargest):
                firstLargest = i
            elif(i<=secondLargest):
                secondLargest = i
            else:
                return True
        return False
      
      
# Time complexity - O(N)
# Space complexity - O(1)
