class Solution(object):
    def checkInclusion(self,pattern,str):
        hashMap={}
        for i in range(len(pattern)):
            hashMap[pattern[i]]=hashMap.get(pattern[i],0)+1
        p = hashMap.copy()
        j=0
        for i in range(len(str)):
            if str[i] in p:
                #print(str[i],p)
                p[str[i]]-=1
            if(i-j+1>=len(pattern)):
                if(all(value == 0 for value in p.values())):
                    return True
                if str[j] in p:
                    p[str[j]]+=1
                j+=1
        return False
      
      
# Time complexity - O(n+m)
# Space complexity - O(k) # k = len(pattern)
        
