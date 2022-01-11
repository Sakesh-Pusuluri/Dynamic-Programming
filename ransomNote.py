class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d={}
        for i in magazine:
            d[i]=d.get(i,0)+1
        for i in ransomNote:
            if(i in d) and (d[i]>0):
                d[i]-=1
            else:
                return False
        return True
            
        
# Time complexity - O(m) # m -> length of magazine
# Space complexity - O(1)
