class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helperCheckPalindrome(s,left,right):
            while(left<right):
                if(s[left]!=s[right]):
                    return False
                left +=1
                right -=1
            return True
            
        left,right = 0,len(s)-1
        while(left<right):
            if(s[left]!=s[right]):
                return helperCheckPalindrome(s,left+1,right) or helperCheckPalindrome(s,left,right-1)
            left +=1
            right -=1
        return True
      
      
# Time complexity - O(N)
# Space complexity - O(1)
        
