class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurence,stack={},[]
        for idx,val in enumerate(s):
            lastOccurence[val] = idx
        for i in range(len(s)):
            while(stack and stack[-1]>s[i] and i<lastOccurence[stack[-1]] and s[i] not in stack):
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
        return ''.join(stack)
        
        
