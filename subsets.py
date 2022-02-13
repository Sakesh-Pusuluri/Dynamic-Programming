class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=[[]]
        for num in nums:
            output+=[ ele+[num] for ele in output]
        return output
