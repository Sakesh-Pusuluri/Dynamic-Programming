class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashMap={}
        leftPointer,ans = 0,0
        stringLength = len(s)
        for rightPointer in range(stringLength):
            hashMap[s[rightPointer]] = hashMap.get(s[rightPointer],0)+1
            if(len(hashMap)>2):
                hashMap[s[leftPointer]] -=1
                if(hashMap[s[leftPointer]]==0):
                    del hashMap[s[leftPointer]]
                leftPointer+=1
            ans = max(ans,rightPointer-leftPointer+1)
        return ans 
                
    
# Time complexity - O(N)
# Space complexity - O(1)
        
