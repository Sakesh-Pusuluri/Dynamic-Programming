class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result=[]
        def backtrack(i,curr_str=''):
            if(len(curr_str)==len(s)):
                result.append(curr_str)
                return
            for i in range(len(s)):
                if(s[i].isalpha()):
                    backtrack(i+1,curr_str+s[i].swapcase())
                backtrack(i+1,curr_str+s[i])
        backtrack(0)
        return result
                
        
        
# Time complexity - O(2^N)

# Space complexity - O(2^N)
