class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        prevEnd,count=0,0
        for i, j in intervals:
            if(prevEnd<j):
                prevEnd=j
                count+=1
        return count
                
        
                
        
