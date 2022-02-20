class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        l=[[intervals[0][0],intervals[0][1]]]
        for i in range(1,len(intervals)):
            for j in range(len(l)):
                if (l[j][0]<=intervals[i][0]<=intervals[i][1]<=l[j][1]):
                    break
            else:
                l.append([intervals[i][0],intervals[i][1]])
        print(l)
        return len(l)
                
        
