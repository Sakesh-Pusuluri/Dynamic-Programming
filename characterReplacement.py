class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        hashMap={}
        maxCount,j,ans=0,0,0
        for i in range(len(string)):
            hashMap[string[i]]=hashMap.get(string[i],0)+1
            maxCount= max(maxCount,hashMap[string[i]])
            while((i-j+1-maxCount)>k):
                hashMap[string[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans
        
# Time complexity = O(N)
# Space complexity = O(k)
