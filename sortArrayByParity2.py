class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if(len(nums)<2):
            return nums
        leftPointer,rightPointer=0,len(nums)-1
        while(leftPointer<rightPointer):
            if(nums[leftPointer]%2!=0 and nums[rightPointer]%2==0):
                nums[leftPointer],nums[rightPointer] = nums[rightPointer],nums[leftPointer]
                leftPointer +=1
                rightPointer -=1
            elif(nums[leftPointer]%2==0):
                leftPointer +=1
            elif(nums[rightPointer]%2!=0):
                rightPointer -=1
        return nums
        
