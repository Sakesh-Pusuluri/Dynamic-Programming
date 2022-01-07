class Solution(object):
    def findAnagrams(self, str, pattern):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        hashMap={}
        l,final_result=[],[]
        for i in range(len(pattern)):
            hashMap[pattern[i]]=hashMap.get(pattern[i],0)+1
        p = hashMap.copy()
        j=0
        for i in range(len(str)):
            if str[i] in p:
                p[str[i]]-=1
            if(i-j+1>=len(pattern)):
                if(all(value == 0 for value in p.values())):
                    final_result.append(j)
                if str[j] in p:
                    p[str[j]]+=1
                j+=1
        return final_result
        
# Time complexity - O(n+m)
# Space complexity - O(k) # k = len(pattern)
