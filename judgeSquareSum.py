import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if(c<2):
            return True
        low,high=0,int(math.sqrt(c))
        while(low<=high):
            result= low*low + high*high
            if(result==c):
                return True
            elif(result<c):
                low+=1
            else:
                high-=1
        return False
        
