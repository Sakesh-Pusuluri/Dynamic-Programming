class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        visited=set()
        count,val = 0,-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    q.append([i,j])
                    visited.add((i,j))
                if(grid[i][j]==1):
                    count+=1
        q.append((-1,-1))
        while(q):
            r,c = q.popleft()
            if r==-1:
                val+=1
                if q:
                    q.append((-1,-1))
            else:
                def adjacent(r,c,count):
                    if(r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1 and (r,c) not in visited):
                        grid[r][c]=2
                        count-=1
                        q.append([r,c])
                        visited.add((r,c))
                        return count
                    return count
                count=adjacent(r-1,c,count)
                count=adjacent(r+1,c,count)
                count=adjacent(r,c-1,count)
                count=adjacent(r,c+1,count)
        if count==0:
            return val
        return -1
