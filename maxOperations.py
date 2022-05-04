class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d,count={},0
        for i,j in enumerate(nums):
            if(k-j in d):
                count+=1
                if(d[k-j]>1):
                    d[k-j]-=1
                else:
                    del d[k-j]
            else:
                d[j] =d.get(j,0)+1
        return count
            
