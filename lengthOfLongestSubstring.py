class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap={}
        stringLength = len(s)
        leftPointer, ans = 0, 0 
        for idx in range(stringLength):
            if(s[idx] not in hashMap):
                hashMap[s[idx]]=idx
            else:
                leftPointer = max(leftPointer,hashMap[s[idx]]+1)
                hashMap[s[idx]]=idx
            ans = max(ans,idx-leftPointer+1)
        return ans
                
        
# Time complexity - O(N)
# Space complexity - O(N)
