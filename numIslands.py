class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited=set()
        islandCount=0
        def dfs(row,col):
            if(row<0 or row==rows or col<0 or col==columns or grid[row][col]!='1'):
                return 
            if((row,col) not in visited):
                visited.add((row,col))
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
        for row in range(rows):
            for col in range(columns):
                if(grid[row][col]=='1' and (row,col) not in visited):
                    dfs(row,col)
                    islandCount+=1
        return islandCount
                    
                
# Time complexity - O(N^2)
