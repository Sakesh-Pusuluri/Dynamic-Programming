class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i,start,end,result=0,0,1,[]
        while(i<len(intervals) and intervals[i][end]<newInterval[start]):
            result.append(intervals[i])
            i+=1
        while(i<len(intervals) and intervals[i][start]<=newInterval[end]):
            newInterval[start] = min(intervals[i][start],newInterval[start])
            newInterval[end] = max(intervals[i][end],newInterval[end])
            i+=1
        result.append(newInterval)
        while(i<len(intervals)):
            result.append(intervals[i])
            i+=1
        return result

      
# Time complexity - O(N)
# Space complexity - O(N)
