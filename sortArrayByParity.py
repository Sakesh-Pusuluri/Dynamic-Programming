class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenList,oddList=[],[]
        for idx in range(len(nums)):
            if(nums[idx]%2==0):
                evenList.append(nums[idx])
            else:
                oddList.append(nums[idx])
        return evenList+oddList
        
