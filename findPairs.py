class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d,output={},0
        for i in nums:
            d[i] = d.get(i,0)+1
        for i in d:
            if(k>0 and i+k in d):
                output+=1
            elif(k==0 and d[i]>1):
                output+=1
        return output
