class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l.append(grid[i][j])
        k=k%(len(grid)*len(grid[0]))
        l=l[-k:]+l[:-k]
        grid2=[]
        z=0
        for i in range(len(grid)):
            p=[]
            for j in range(len(grid[0])):
                p.append(l[z])
                z+=1
            grid2.append(p)
        return grid2
