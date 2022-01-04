class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def backtrack(i,curr_list=[]):
            if(len(curr_list)==k):
                result.append(curr_list[:])
                return
            for j in range(i,n+1):
                curr_list.append(j)
                backtrack(j+1,curr_list)
                curr_list.pop()
        backtrack(1)
        return result
      
# Time complexity - O(n^2)
# Space complexity - O(n)
