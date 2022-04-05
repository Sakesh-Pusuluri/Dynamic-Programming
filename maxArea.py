class Solution(object):
    def maxArea(self, height):
        n = len(height)-1
        leftPointer,rightPointer,ans =0,n,0
        while(leftPointer<rightPointer):
            value = min(height[leftPointer],height[rightPointer])
            ans = max(ans,n*value)
            if(height[leftPointer]>height[rightPointer]):
                rightPointer -=1
            else:
                leftPointer +=1
            n -=1
        return ans 
            
        
