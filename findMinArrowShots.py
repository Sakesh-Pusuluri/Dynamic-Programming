class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        arr = 1
        firstEnd=points[0][1]
        for start,end in points:
            if(firstEnd<start):
                arr+=1
                firstEnd=end
        return arr
        
        
# Time complexity - O(NlogN)
# Space complexity - O(N)
