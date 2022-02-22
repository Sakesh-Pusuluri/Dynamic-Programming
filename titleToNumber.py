class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        alphaMap={chr(i+65):i+1 for i in range(26)}
        n=len(columnTitle)
        for i in range(n):
            currChar=columnTitle[n-1-i]
            result+=alphaMap[currChar]*(26**i)
        return result
