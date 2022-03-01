class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for i in nums:
            n=len(result)
            for j in range(n):
                result.append(result[j]+[i])
        return result
            
# Time complexity - O(N*2^N)
