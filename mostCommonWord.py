import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^A-Za-z]',' ',paragraph).lower().split()
        banned = set(banned)
        d = {}
        for word in paragraph:
            if word not in banned:
                d[word] = d.get(word,0)+1
        return max(d,key=d.get)
        
