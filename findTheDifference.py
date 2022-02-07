class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i] = d.get(i,0)+1
        for i in s:
            if(d[i]==1):
                del d[i]
            else:
                d[i]-=1
        return list(d.keys())[0]
        
