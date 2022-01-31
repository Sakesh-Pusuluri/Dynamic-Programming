class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=float('-inf')
        for i in accounts:
            ans=max(ans,sum(i))
        return ans
        
