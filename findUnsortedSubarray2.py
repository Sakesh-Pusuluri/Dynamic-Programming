class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftPointer, rightPointer = 0, len(nums)-1
        while(leftPointer<len(nums)-1 and nums[leftPointer]<=nums[leftPointer+1]):
            leftPointer +=1
        if(leftPointer==len(nums)-1):
            return 0
        while(rightPointer>0 and nums[rightPointer]>=nums[rightPointer-1]):
            rightPointer -=1
        _min,_max = math.inf, - math.inf
        for idx in range(leftPointer,rightPointer+1):
            _min = min(_min,nums[idx])
            _max = max(_max,nums[idx])
        while(leftPointer>0 and nums[leftPointer-1]>_min):
            leftPointer -=1
        while(rightPointer<len(nums)-1 and nums[rightPointer+1]<_max):
            rightPointer +=1
        return rightPointer-leftPointer+1
