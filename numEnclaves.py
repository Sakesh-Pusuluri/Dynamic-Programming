class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows  = len(grid)
        columns =len(grid[0])
        count=0
        def dfs(row,col):
            if(row<0 or row==rows or col<0 or col==columns or grid[row][col]!=1):
                return 
            grid[row][col]=-1
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
                
        for row in range(rows):
            for col in range(columns):
                if(grid[row][col]==1 and (row in [0,rows-1] or col in [0,columns-1])):
                    dfs(row,col)
        print(grid)
        for row in range(rows):
            for col in range(columns):
                if(grid[row][col]==1):
                    count+=1
                    
        return count
        
                
        
        
