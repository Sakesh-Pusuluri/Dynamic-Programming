class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.upper()==word):
            return True
        elif(word.lower()==word):
            return True
        elif(word[0].isupper() and word[1:].islower()):
            return True
        return False
        
