class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if(len(s)<k):
            return 0
        slow,fast,count,idx=0, 0,0,0
        charDict={}
        while(fast<len(s)):
            if not s[fast] in charDict:
                charDict[s[fast]]=idx
            else:
                slow=max(slow,charDict[s[fast]]+1)
                charDict[s[fast]]=idx
            if(fast-slow+1==k):
                count+=1
                del charDict[s[slow]]
                slow+=1
            idx+=1
            fast+=1
        return count
                
        
        
