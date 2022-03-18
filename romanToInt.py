class Solution:
    def romanToInt(self, s: str) -> int:
        integerDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        finalResult,ans = [],0
        for string in s:
            finalResult.append(integerDict[string])
        for i in range(len(finalResult)):
            if(i>0 and finalResult[i]>finalResult[i-1]):
                ans = ans + (finalResult[i] - 2*finalResult[i-1])
            else:
                ans +=finalResult[i]
        return ans
            
