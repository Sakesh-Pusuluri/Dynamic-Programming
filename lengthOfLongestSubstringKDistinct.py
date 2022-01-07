class Solution:
    def lengthOfLongestSubstringKDistinct(self, str1: str, k: int) -> int:
        if(k>=len(str1)):
            return len(str1)
        ans,j=0,0
        s=''
        d={}
        for i in range(len(str1)):
            if str1[i] in d :
                s+=str1[i]
                d[str1[i]]+=1
            else:
                s+=str1[i]
                d[str1[i]]=1
            while(len(d)>k):
                d[str1[j]]-=1
                if(d[str1[j]]==0):
                    del d[str1[j]]
                s=s[1:]
                j+=1
            ans=max(ans,i-j+1)
        return ans
      
      
# Time complexity - O(n)
# Space complexity - O(k)
