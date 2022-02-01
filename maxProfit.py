class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max,_min = 0,float('inf')
        for i in prices:
            _min = min(i,_min)
            profit = i-_min
            _max = max(_max,profit)
        return _max
            
        
# Time complexity - O(N)
# Space complexity - O(1)
