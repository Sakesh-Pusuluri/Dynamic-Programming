class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if stack:
                    if(stack and  (stack[-1]=='(' and i==')') or (stack[-1]=='{' and i=='}') or (stack[-1]=='[' and i==']')):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack)==0
