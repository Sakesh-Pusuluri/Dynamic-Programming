class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        result=[-1]
        j=0
        for idx in range(len(pushed)):
            result.append(pushed[idx])
            while(j<len(popped) and popped[j]==result[-1]):
                result.pop()
                j+=1
        if(result!=[-1]):
            return False
        return True
