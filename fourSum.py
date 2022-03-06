class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for idx in range(len(nums)):
            #if(idx==0 or nums[idx-1]!=nums[idx]):
            for j in range(idx+1,len(nums)):
                #if(nums[j-1]!=nums[j]):
                _sum = target- (nums[idx] + nums[j])
                leftPointer,rightPointer = j+1,len(nums)-1
                while(leftPointer<rightPointer):
                    value = nums[leftPointer] + nums[rightPointer]
                    if(value == _sum):
                        result.append([nums[idx],nums[j],nums[leftPointer],nums[rightPointer]])
                        leftPointer +=1
                        rightPointer -=1
                        while(leftPointer<rightPointer and nums[leftPointer-1]==nums[leftPointer]):
                            leftPointer += 1
                        while(leftPointer<rightPointer and nums[rightPointer+1]==nums[rightPointer]):
                            rightPointer -= 1
                    elif(value<_sum):
                        leftPointer +=1
                    else:
                        rightPointer -=1
        return set(tuple(row) for row in result)
