class Solution:
    def __init__(self):
        self._max=-1
    def maxDistance(self, grid: List[List[int]]) -> int:
        q=deque()
        visited = set()
        _max=-1
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if(grid[row][column]==1):
                    q.append((row,column))
                    visited.add((row,column))
        while q:
            row,column = q.popleft()
            value = grid[row][column]
            def adjacent(row,column,value,_max):
                if(0<=row<len(grid) and 0<=column<len(grid[0]) and (row,column) not in visited):
                    grid[row][column] = 1+ value
                    self._max = max(_max,grid[row][column])
                    q.append((row,column))
                    visited.add((row,column))
            adjacent(row-1,column,value,_max)
            adjacent(row+1,column,value,_max)
            adjacent(row,column-1,value,_max)
            adjacent(row,column+1,value,_max)
        if(self._max==-1):
            return -1
        return self._max-1
        
        
        
# Time complexity - O(rows*columns)
# Space complexity - O(rows*columns)
