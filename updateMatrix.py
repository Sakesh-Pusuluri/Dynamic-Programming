class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        visited=set()
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                if(mat[row][column]==0):
                    q.append((row,column))
                    visited.add((row,column))
        while q:
            row,column = q.popleft()
            value=mat[row][column]
            def adjacent(row,column,value):
                if(0<=row<len(mat) and 0<=column<len(mat[0]) and (row,column) not in visited):
                    mat[row][column] = 1+ value
                    q.append((row,column))
                    visited.add((row,column))
            adjacent(row-1,column,value)
            adjacent(row+1,column,value)
            adjacent(row,column-1,value)
            adjacent(row,column+1,value)
            
        return mat
                
        
# Time complexity -  O(rows*columns)
# Space complexity - O(rows*columns)
