class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        for i in s:
            dict_s[i]=dict_s.get(i,0)+1
        dict_t={}
        for i in t:
            dict_t[i]=dict_t.get(i,0)+1
        return dict_s==dict_t
            
        
        
# Time complexity - O(max(m,n))

# Space complexity - O(1)
