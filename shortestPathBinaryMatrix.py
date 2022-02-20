class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q=deque()
        visited=set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if(grid[row][column]==1):
                    grid[row][column]='x'
        q.append((0,0))
        visited.add((0,0))
        if(grid[0][0]=='x' or grid[-1][-1]=='x'):
            return -1
        if(len(grid)==1):
            return 1
        while(q):
            row,column=q.popleft()
            value=grid[row][column]
            def adjacent(row,column,value):
                if(0<=row<len(grid) and 0<=column<len(grid[0]) and (row,column) not in visited and grid[row][column]!='x'):
                    grid[row][column]=1+value
                    q.append((row,column))
                    visited.add((row,column))
            adjacent(row-1,column,value)
            adjacent(row+1,column,value)
            adjacent(row,column-1,value)
            adjacent(row,column+1,value)
            adjacent(row-1,column-1,value)
            adjacent(row-1,column+1,value)
            adjacent(row+1,column-1,value)
            adjacent(row+1,column+1,value)
        if grid[-1][-1]==0:
            return -1
        return grid[-1][-1]+1
                    
            
            
        
