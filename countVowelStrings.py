class Solution:
    def countVowelStrings(self, n: int) -> int:
        if(n==0):
            return 
        else:
            result=[1]*5
            for num in range(n):
                for idx in range(1,5):
                    result[idx]+=result[idx-1]
        return result[-1]
            
            
