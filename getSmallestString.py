class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result=['a']*n
        value = n
        for idx in range(n-1,-1,-1):
            if value == k:
                break
            result[idx] = chr(96+min(k - value +1,26))
            value += ord(result[idx]) - 96 -1
        return ''.join(result)
      
# Time complexity - O(n)
# Space complexity - O(n)
