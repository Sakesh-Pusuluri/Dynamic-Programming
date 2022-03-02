class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sourceLength,targetLength = len(s),len(t)
        leftPointer=rightPointer=0
        while(leftPointer<sourceLength and rightPointer<targetLength):
            if(s[leftPointer]==t[rightPointer]):
                leftPointer+=1
            rightPointer+=1
        return leftPointer==len(s)
