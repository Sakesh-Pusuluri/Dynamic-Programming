class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count,leftPointer,rightPointer=0,0,0
        while(rightPointer<len(s)):
            if(s[rightPointer]!=s[leftPointer]):
                leftPointer = rightPointer
            if(rightPointer-leftPointer==k-1):
                count+=1
                l=s[:leftPointer]+s[rightPointer+1:]
                rightPointer-=2*k
                if(rightPointer<0):
                    rightPointer=0
                leftPointer=rightPointer
                s=l
            rightPointer+=1
        return s
