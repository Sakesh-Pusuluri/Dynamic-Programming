class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited=set()
        count=0
        def dfs1(row,col):
            if(row<0 or row==rows or col<0 or col==columns):
                return 
            if(grid[row][col]==0):
                grid[row][col]=1
                dfs1(row-1,col)
                dfs1(row+1,col)
                dfs1(row,col-1)
                dfs1(row,col+1)
        for row in range(rows):
            for col in range(columns):
                if(grid[row][col]==0 and (row in [0,rows-1] or col in [0,columns-1])):
                    dfs1(row,col)
        
        def dfs(row,col):
            if(row<0 or row==rows or col<0 or col==columns or (row,col) in visited):
                return 
            if(grid[row][col]==0):
            visited.add((row,col))
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        for row in range(rows):
            for col in range(columns):
                if(grid[row][col]==0 and (row,col) not in visited):
                    dfs(row,col)
                    count+=1
        return count
                    
                    
                    
